# Al-Aziz Education Platform

A learning-center management application built with Django REST Framework and React.

O'quv markazi uchun o'quvchilar, kurslar, davomat, baholar va dars jadvalini boshqarish platformasi.

**Stack:** Python · Django · Django REST Framework · JWT · PostgreSQL · React · Vite

## Features

- Accounts and interfaces for students and teachers.
- Students, class groups, subjects and course enrollments.
- Attendance, grades and class schedules.
- Dashboard reports and attendance/grade exports.
- JWT login, token refresh and profile management.
- Django admin for managing application data.

## Run locally

Use Python 3.12 and Node.js 22.12+. PostgreSQL is the default database; a SQLite quick-start option is included below.

```bash
git clone https://github.com/NurmuhammaddAliyev/Al-Aziz_education_platform.git
cd Al-Aziz_education_platform
python -m venv .venv
```

Activate with `.venv\Scripts\Activate.ps1` on Windows PowerShell or `source .venv/bin/activate` on macOS/Linux.

### 1. Install backend dependencies

```bash
python -m pip install -r requirements.txt
```

### 2. Configure the environment

Copy `bacend/.env.example` to `bacend/.env`. Generate a local secret:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Paste the generated value into `SECRET_KEY` in `bacend/.env`. For PostgreSQL, create a database and fill in `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST` and `DB_PORT`.

For a quick local demo without PostgreSQL, set:

```dotenv
DB_ENGINE=django.db.backends.sqlite3
DB_NAME=db.sqlite3
DEBUG=True
```

The relative SQLite database path is resolved from your working directory; run the backend commands below from the repository root.

### 3. Start the backend

```bash
python bacend/manage.py migrate
python bacend/manage.py createsuperuser
python bacend/manage.py runserver
```

Admin: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

### 4. Start the frontend

In a second terminal, from the repository root:

```bash
cd bacend/frontend
npm ci
npm run dev
```

Open the URL printed by Vite, normally [http://localhost:5173](http://localhost:5173). The API client currently targets `http://127.0.0.1:8000`.

## Structure

| Path | Responsibility |
| --- | --- |
| `bacend/accounts/` | Accounts, JWT registration and profiles |
| `bacend/students/` | Students, groups and enrollments |
| `bacend/subjects/` | Course subjects |
| `bacend/attendance/` | Attendance |
| `bacend/grades/` | Grades |
| `bacend/schedule/` | Class timetable |
| `bacend/reports/` | Reports and exports |
| `bacend/frontend/` | React interface |

The backend directory is named `bacend` in this repository; use that exact spelling in commands.

## Main API routes

- `/api/auth/token/` and `/api/auth/token/refresh/`
- `/api/auth/register/` and `/api/auth/me/`
- `/api/students/`, `/api/class-groups/`, `/api/enrollments/`
- `/api/subjects/`, `/api/attendance/`, `/api/grades/`
- `/api/schedule/` and `/api/reports/`

## Checks

From the repository root, with the backend environment configured:

```bash
python bacend/manage.py check
python bacend/manage.py test accounts
```

Authentication tests cover registration/password hashing, a usable JWT profile request, rejected login and anonymous write protection. They are a starting point, not complete application coverage.

From `bacend/frontend/`:

```bash
npm run build
npm run lint
```

## Deployment notes

Configure a production database, a unique `SECRET_KEY`, `DEBUG=False` and explicit allowed hosts/origins. The frontend API URL is currently defined in [Api.js](bacend/frontend/src/services/Api.js) and must be adapted for a hosted backend. Review role-assignment and object-level permissions before exposing real student data.

## Author

[Nurmuhammad Aliyev](https://github.com/NurmuhammaddAliyev) · [Telegram](https://t.me/nurmuhammad252505)
