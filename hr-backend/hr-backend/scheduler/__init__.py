from apscheduler.schedulers.asyncio import AsyncIOScheduler
from core.email_bot import EmailBot
from core.email_bot.settings import EmailBotSettings
from loguru import logger
from agents.candidate import CandidateProcessAgent
from langchain.messages import HumanMessage
from settings import settings
from core.cache import HRCache
from sqlalchemy import select
from models import AsyncSessionFactory
from models.candidate import CandidateModel
from schemas.candidate_schema import CandidateSchema
from schemas.position_schema import PositionSchema
from schemas.user_schema import UserSchema

scheduler = AsyncIOScheduler()


async def poll_and_process_emails(bot: EmailBot, state: dict):
    try:
        last_uid = state.get("last_uid")
        if last_uid is None:
            last_uid = await bot.get_max_uid() or 0
        state["last_uid"] = last_uid
        logger.info(f"Initialized last_uid={last_uid}")

        new_emails = await bot.fetch_since_uid(last_uid)
        if not new_emails:
            return

        new_emails.sort(key=lambda e: int(e.uid))

        for mail in new_emails:
            if mail.from_.address.lower() == bot.settings.email.lower():
                continue

            thread_id = mail.from_.address
            async with AsyncSessionFactory() as session:
                async with session.begin():
                    stmt = select(CandidateModel).where(CandidateModel.email == thread_id)
                    result = await session.scalars(stmt)
                    candidates = result.all()
                    if not candidates:
                        logger.warning(f"No candidate for {thread_id}")
                        state["last_uid"] = max(state["last_uid"], int(mail.uid))
                        cache = HRCache()
                        await cache.set_email_last_uid(state["last_uid"])
                        continue

                    c = candidates[0]
                    candidate_schema = CandidateSchema.model_validate(c)
                    position_schema = PositionSchema.model_validate(c.position)
                    interviewer_schema = UserSchema.model_validate(c.position.creator)

                    async with CandidateProcessAgent(
                        candidate=candidate_schema,
                        position=position_schema,
                        interviewer=interviewer_schema,
                    ) as agent:
                        response = await agent.ainvoke(
                            messages=[HumanMessage(content=f"receive email: {mail.text or mail.html}")],
                            thread_id=thread_id
                        )
                        logger.info(f"Processed email from {thread_id}")

            state["last_uid"] = max(state["last_uid"], int(mail.uid))
            cache = HRCache()
            await cache.set_email_last_uid(state["last_uid"])

        logger.info(f"Processed {len(new_emails)} new emails")

    except Exception as e:
        logger.exception(f"Failed to poll and process emails: {e}")


async def start_email_polling():
    email_settings = EmailBotSettings(
        imap_host=settings.EMAIL_BOT_IMAP_HOST,
        smtp_host=settings.EMAIL_BOT_SMTP_HOST,
        email=settings.EMAIL_BOT_EMAIL,
        password=settings.EMAIL_BOT_PASSWORD,
    )
    cache = HRCache()
    last_uid = await cache.get_email_last_uid()
    state: dict = {"last_uid": last_uid}

    bot = EmailBot(email_settings)
    await bot.connect()

    scheduler.add_job(poll_and_process_emails, "interval", seconds=15, args=[bot, state], max_instances=1)
    scheduler.start()
    logger.info("Scheduler started, polling inbox...")
    return bot, scheduler
