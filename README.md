# 📋 Task Management REST API

## 📌 Project Description

This project is a RESTful API built using Flask for managing tasks. It allows users to register, authenticate using JWT tokens, and perform CRUD operations on tasks.

The API follows REST principles and supports JSON-based communication, making it suitable for frontend or mobile integrations.

---

## 🚀 Features

- User Registration & Login (JWT Authentication)
- Secure API with Token-Based Access
- Create, Read, Update, Delete Tasks (CRUD)
- JSON Request & Response Handling
- Modular Flask Project Structure
- SQLite Database Integration
- Basic Input Validation
- Organized API Endpoints

---

## 🛠️ Tech Stack

- Python
- Flask
- Flask-SQLAlchemy
- Flask-JWT-Extended
- Marshmallow
- SQLite

---

## 📂 Project Structure

```
task-api/
│── app/
│ ├── init.py
│ ├── extensions.py
│ ├── models.py
│
│ ├── auth/
│ ├── tasks/
│ ├── users/
│ ├── utils/
│
│── config.py
│── run.py
│── requirements.txt
│── README.md

```

---

## ⚙️ Setup Instructions

### 1. Clone Repository
git clone <your-repo-link>
cd task-api

---

### 2. Create Virtual Environment
python -m venv venv

**Activate: For Windows**
venv\Scripts\activate

---

### 3. Install Dependencies
pip install -r requirements.txt

---

### 4. Initialize Database

Open Python shell:

```python
from app import create_app
from app.extensions import db

app = create_app()
app.app_context().push()

db.create_all()
```

### 5. Run Application
python run.py

### 6. Access API
http://127.0.0.1:5000

---

### 🔐 Authentication

This API uses JWT tokens.

Login Flow:

1.Register user

2.Login to get token

3.Use token in headers

Header Format:
```
Authorization: Bearer <your_token>

```
---

### 📌 API Endpoints
🔐 Authentication
Register User
---
POST /api/auth/register
---
Login User
---
POST /api/auth/login
---

---

### 📋 Tasks

Get All Tasks
```
GET /api/tasks/
```
Create Task
```
POST /api/tasks/
```
Update Task
```
PUT /api/tasks/<id>
```
Delete Task
```
DELETE /api/tasks/<id>
```
---

### 👥 Users
Get All Users
```
GET /api/users/
```
---

### 📊 Sample Request
Create Task
```
{
  "title": "Complete API project",
  "description": "Finish Flask REST API"
}
```
---

### 📊 Sample Response
```
{
  "id": 1,
  "title": "Complete API project",
  "description": "Finish Flask REST API",
  "status": "pending",
  "priority": "medium"
}
```
---

### ❗ Error Handling

200 → Success

201 → Created

400 → Bad Request

401 → Unauthorized

404 → Not Found

---

### Testing

Use tools like:

-Postman

-Thunder Client (VS Code)

-curl

---


### 🎯 What I Learned

-REST API Design

-JWT Authentication

-Flask Backend Development

-JSON Data Handling

-Database Integration

-API Testing

---

### 📌 Future Improvements

Pagination & Filtering

Swagger API Documentation

Rate Limiting

Role-Based Access Control

Task Categories & Tags

Deployment (Render / Railway)