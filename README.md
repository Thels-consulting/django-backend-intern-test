# Django Backend Intern Assessment — Employee Management API

Welcome! This is a take-home technical assessment for the Django backend intern role. You'll build a small but realistic REST API for managing departments and employees using Django and Django REST Framework.

## Tech stack

- Python 3.12+
- Django 5.2+ / 6.x
- Django REST Framework
- django-filter
- SQLite (no external database needed)

## Step 1 — Fork this repository

Click **Fork** at the top right of this repository's GitHub page. This creates your own copy under your GitHub account — that copy is your submission, and you'll work entirely inside it.

Do not request write access to this original repository. You will submit your work as a Pull Request from your fork (see below).

## Step 2 — Open your fork in GitHub Codespaces

1. Go to your forked repository on GitHub.
2. Click the green **Code** button, then the **Codespaces** tab.
3. Click **Create codespace on main**.
4. Wait for the container to build — it will automatically install dependencies and run migrations for you (see `.devcontainer/devcontainer.json`).
5. Once the terminal is ready, start the dev server to confirm everything works:
   ```bash
   python manage.py runserver
   ```
   Codespaces will prompt you to open the forwarded port (8000) in a browser.

You can also work locally instead of Codespaces if you prefer (see below), but Codespaces requires no local setup at all.

### Local setup (optional alternative to Codespaces)

```bash
git clone <your-fork-url>
cd django-backend-intern-test
python -m venv venv
source venv/Scripts/activate   # Windows Git Bash
# or: source venv/bin/activate  # macOS/Linux
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Step 3 — Complete the assessment

Build out the `employees` app. The models, serializers, views, and URLs are currently stubs with `TODO` comments — that's what you're implementing.

### Models

**Department**
| Field | Notes |
|---|---|
| `id` | auto |
| `name` | required, unique |
| `description` | optional |
| `created_at` | set automatically on creation |

**Employee**
| Field | Notes |
|---|---|
| `id` | auto |
| `first_name` | required |
| `last_name` | required |
| `email` | required, unique, must be a valid email |
| `phone` | optional |
| `department` | ForeignKey to `Department` |
| `job_title` | optional |
| `salary` | required, cannot be negative |
| `date_joined` | set automatically on creation |
| `is_active` | defaults to `True` |
| `created_at` | set automatically on creation |

### API endpoints

**Departments**

```
GET    /api/departments/
POST   /api/departments/
GET    /api/departments/<id>/
PUT    /api/departments/<id>/
DELETE /api/departments/<id>/
```

**Employees**

```
GET    /api/employees/
POST   /api/employees/
GET    /api/employees/<id>/
PUT    /api/employees/<id>/
DELETE /api/employees/<id>/
```

### Validation

The API must reject, with an appropriate 4xx status code:

- A duplicate employee email.
- An invalid email format (e.g. `not-an-email`).
- A negative salary (e.g. `{"salary": -50000}`).
- An employee referencing a `department` id that doesn't exist.

### Filtering

```
GET /api/employees/?department=1
GET /api/employees/?is_active=true
```

### Search

```
GET /api/employees/?search=john
```

Search should match against `first_name`, `last_name`, `email`, and `job_title`.

### Authentication

- Unauthenticated users **can**: `GET` employees and departments (list and detail).
- Only authenticated users **can**: `POST`, `PUT`, `DELETE` on employees and departments.

You can use Django's built-in `SessionAuthentication` or `BasicAuthentication` — nothing more elaborate (like JWT) is required. To create a user for testing:

```bash
python manage.py createsuperuser
```

DRF's browsable API login is available at `/api-auth/login/`.

### Bonus (optional)

Want to go further? These aren't required, but are a nice way to stand out:

- **Swagger / OpenAPI docs** — add interactive API documentation (e.g. via `drf-spectacular` or `drf-yasg`) exposed at a route like `/api/docs/`.
- **Automated tests** — write tests covering things like: department creation, employee creation, employee listing/retrieval, duplicate email validation, negative salary validation, department filtering, and authentication restrictions. Run them with:

  ```bash
  python manage.py test
  ```

  A GitHub Actions workflow (`.github/workflows/tests.yml`) runs this automatically on every push and pull request — if you add tests, check the **Actions** tab on your fork to confirm they pass.

## Git commit expectations

Use multiple small, focused commits rather than one giant commit at the end. Commit messages should follow:

```
type: short description
```

Recommended types: `feat`, `fix`, `test`, `docs`, `refactor`, `chore`.

Good:

```
feat: add department model
feat: implement employee API
feat: add employee validation
test: add employee API tests
docs: update README
```

Avoid vague messages like `update`, `changes`, `fix`, `final`, `final2`, `stuff`.

## Submitting your work

1. Commit and push your work to **your fork**.
2. Open a Pull Request from your fork back to this original repository.
3. PR title:
   ```
   [SUBMISSION] Full Name and email in bracket
   ```
4. PR description, using this template:

   ```markdown
   ## Completed Features

   - [x] Department model
   - [x] Employee model
   - [x] Department API
   - [x] Employee API
   - [x] Validation
   - [x] Filtering
   - [x] Search
   - [x] Authentication
   - [x] Documentation

   ## Bonus (optional)

   - [ ] Swagger / OpenAPI docs
   - [ ] Automated tests

   ## Testing

   Command:
   python manage.py test

   Result:
   All tests passing. (or: No tests added.)

   ## Notes

   Mention any assumptions, limitations, or additional features.
   ```

   Check off only what you actually completed.

The Pull Request itself is your official submission — you don't need to send anything separately.

## AI policy

AI tools may be used during this assessment. However, you are responsible for understanding and being able to explain all submitted code. During a follow-up technical interview, you may be asked to explain design decisions, debug your implementation, or modify part of your solution.

## Security warning

Do **not** commit passwords, API keys, tokens, secrets, or credentials of any kind. If you need a secret value locally (you shouldn't for this assessment), keep it in a `.env` file — it's already excluded via `.gitignore`.
