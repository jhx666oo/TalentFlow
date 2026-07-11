"""配置模块单元测试"""

from settings import settings


class TestSettings:
    """验证配置加载正常工作"""

    def test_database_url_is_built(self):
        """DATABASE_URL 由 computed_field 自动拼接"""
        url = settings.DATABASE_URL
        assert url.startswith("postgresql+psycopg://")
        assert "@" in url
        assert settings.DB_HOST in url

    def test_jwt_secret_is_set(self):
        """JWT_SECRET_KEY 不为空"""
        assert settings.JWT_SECRET_KEY

    def test_redis_config(self):
        """Redis 配置有效"""
        assert settings.REDIS_HOST
        assert settings.REDIS_PORT > 0

    def test_resume_dir_is_absolute(self):
        """简历目录路径是绝对路径"""
        import os
        assert os.path.isabs(settings.RESUME_DIR)

    def test_token_expiry_is_reasonable(self):
        """Token 过期时间配置合理"""
        assert settings.JWT_ACCESS_TOKEN_EXPIRES.days >= 1
        assert settings.JWT_REFRESH_TOKEN_EXPIRES.days >= 7

    def test_debug_defaults_to_false(self):
        """生产环境 DEBUG 默认 False"""
        assert settings.DEBUG is False
