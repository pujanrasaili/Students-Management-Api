# Student Management REST API

A professional REST API built with **Python Flask** for managing student records at Bedfordshire University. Features JWT authentication, full CRUD operations, search/filter capabilities, and auto-generated Swagger documentation.

---

## Features

- **Full REST API** — GET, POST, PUT, DELETE for student records
- **JWT Authentication** — Secure login with password hashing
- **Search & Filter** — Search students by name, ID, or course
- **Statistics Endpoint** — Total students, average GPA, students per course
- **Swagger UI Docs** — Auto-generated API documentation at `/docs`
- **SQLite Database** — Lightweight, zero-config database
- **Professional Error Handling** — Clean JSON error responses

---

## Tech Stack

| Technology | Purpose |
|------------|---------|
| Python + Flask | Web framework |
| Flask-SQLAlchemy | ORM & database management |
| Flask-JWT-Extended | JWT authentication |
| Werkzeug | Password hashing |
| Flasgger | Swagger UI documentation |
| SQLite | Database |

---

## Project Structure

```
student-management-api/
│
├── app.py              # Main application entry point
├── config.py           # Configuration (DB, JWT, secret keys)
├── models.py           # Database models (User, Student)
├── auth.py             # Authentication routes (register, login)
├── routes.py           # Student CRUD routes
├── requirements.txt    # Python dependencies
├── .gitignore          # Git ignore rules
└── README.md           # Project documentation
```

---

## Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/pujanrasaili/Students-Management-Api.git
cd Students-Management-Api
```

### 2. Create a virtual environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the application
```bash
python app.py
```

The API will be running at `http://127.0.0.1:5000`

---

## 📖 API Documentation

Once running, visit **[http://127.0.0.1:5000/docs](http://127.0.0.1:5000/docs)** for the interactive Swagger UI.

---

## Authentication

All student endpoints require a valid JWT token. Follow these steps:

### Step 1 — Register a user
```http
POST /api/register
Content-Type: application/json

{
  "username": "admin",
  "password": "yourpassword"
}
```

### Step 2 — Login to get a token
```http
POST /api/login
Content-Type: application/json

{
  "username": "admin",
  "password": "yourpassword"
}
```

**Response:**
```json
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "message": "Login successful"
}
```

### Step 3 — Use the token in requests
```http
Authorization: Bearer <your_token>
```

---

## 📡 API Endpoints

### Auth

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/register` | Register a new user |
| `POST` | `/api/login` | Login and receive JWT token |

### Students *(requires JWT)*

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/students` | Get all students (supports search & filter) |
| `POST` | `/api/students` | Add a new student |
| `GET` | `/api/students/<id>` | Get a specific student by ID |
| `PUT` | `/api/students/<id>` | Update a student |
| `DELETE` | `/api/students/<id>` | Delete a student |
| `GET` | `/api/students/stats` | Get statistics (total, avg GPA, per course) |

---

## 📝 Example Requests

### Add a student
```http
POST /api/students
Authorization: Bearer <token>
Content-Type: application/json

{
  "student_id": "BED001",
  "first_name": "Pujan",
  "last_name": "Rasaili",
  "email": "pujan@beds.ac.uk",
  "course": "Software Engineering",
  "year": 2,
  "gpa": 3.8
}
```

### Search students
```http
GET /api/students?search=pujan&course=Software
Authorization: Bearer <token>
```

### Get statistics
```http
GET /api/students/stats
Authorization: Bearer <token>
```

**Response:**
```json
{
  "total_students": 42,
  "average_gpa": 3.45,
  "students_per_course": {
    "Software Engineering": 15,
    "Computer Science": 12,
    "Data Science": 10,
    "Cybersecurity": 5
  }
}
```

---

## Data Models

### User
| Field | Type | Notes |
|-------|------|-------|
| id | Integer | Primary key |
| username | String(80) | Unique |
| password | String(200) | Hashed |
| role | String(20) | Default: 'admin' |

### Student
| Field | Type | Notes |
|-------|------|-------|
| id | Integer | Primary key |
| student_id | String(20) | Unique |
| first_name | String(50) | Required |
| last_name | String(50) | Required |
| email | String(100) | Unique |
| course | String(100) | Required |
| year | Integer | Required |
| gpa | Float | Default: 0.0 |

---

## Author

**Pujan Rasaili**
Bedfordshire University — Software Engineering

---

## License

This project is for academic and portfolio purposes.
