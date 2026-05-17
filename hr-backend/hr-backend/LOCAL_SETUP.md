# Local Setup

## Backend

This backend expects:

- Python 3.13 preferred
- PostgreSQL
- Redis

Create a local env file from `.env.example` and fill in the required secrets.

Recommended local database names:

- `hr_system`
- `hr_system_agent`

Recommended local Redis port:

- `6389`

## Backend Commands

Create a virtual environment:

```bash
python3.13 -m venv .venv-macos
```

Install dependencies:

```bash
./.venv-macos/bin/pip install -r requirements.txt
```

Run database migrations:

```bash
./.venv-macos/bin/alembic upgrade head
```

Initialize seed data:

```bash
./.venv-macos/bin/python init_data.py
```

Start the backend:

```bash
./.venv-macos/bin/uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

## Frontend

The frontend development API target is already configured in `.env.development`:

```bash
VITE_API_BASE_URL=http://127.0.0.1:8000
```

Install dependencies:

```bash
npm install
```

Start the frontend:

```bash
npm run dev
```

## Default Seed Accounts

After `init_data.py` runs successfully, these accounts should exist:

- `Boss / 111111`
- `hr / 111111`
- `tech / 111111`
- `operator / 111111`
- `market / 111111`
- `finance / 111111`
- `legal / 111111`
- `admin / 111111`
- `service / 111111`
