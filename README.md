# 📌 Job Tracker

Job Tracker is a basic pet project that allows users to register, log in, and manage a list of job vacancies. It supports JWT authentication and basic CRUD operations for vacancies.

---

## 🚀 Tech Stack

- **Frontend**: React, React Router, Axios
- **Backend**: FastAPI
- **Database**: PostgreSQL (main), SQLite (tests)
- **Auth**: JWT (OAuth2 PasswordBearer)
- **Validation**: Pydantic v2
- **Testing**: Pytest
- **Dev Server**: Vite (frontend), Uvicorn (backend)

> ⚠️ This is a basic implementation meant for learning and portfolio purposes.

---

## ⚙️ Backend Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/job-tracker.git
cd job-tracker
```

### 2. Create a virtual environment and activate it

```bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate    # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file

```env
DATABASE_URL=postgresql://postgres:yourpassword@localhost/jobtracker
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 5. Run the backend server

The database tables are automatically created at startup using SQLAlchemy.

```bash
uvicorn main:app --reload
```

---

## 🧪 Running Tests

Run tests using SQLite in-memory:

```bash
PYTHONPATH=./backend pytest -v
```

---

## 📬 API Endpoints

| Method | Endpoint         | Description                | Auth |
|--------|------------------|----------------------------|------|
| POST   | /users/register  | Register new user          | ❌   |
| POST   | /users/login     | Get JWT token              | ❌   |
| GET    | /vacancies       | Get all vacancies          | ✅   |
| POST   | /vacancies       | Create new vacancy         | ✅   |
| PUT    | /vacancies/{id}  | Update vacancy by ID       | ✅   |
| DELETE | /vacancies/{id}  | Delete vacancy by ID       | ✅   |

---

## ✍️ Author

Anastasia Tolmacheva