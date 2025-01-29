# HNG_Task0
# FastAPI ISO 8601 Timestamp API

## 📌 Project Description
This is a simple **FastAPI** application that returns a JSON response containing:
- An email address.
- The current **ISO 8601 formatted datetime** in UTC.
- A link to the project's GitHub repository.

## 🚀 Setup Instructions

### **1️⃣ Install Dependencies**
Ensure you have **Python 3.8+** installed, then install FastAPI and Uvicorn:
```sh
pip install fastapi uvicorn
```

### **2️⃣ Initialize `requirements.txt`**
To create a `requirements.txt` file, run:
```sh
pip freeze > requirements.txt
```
This will save all installed dependencies.

To install dependencies from `requirements.txt`, use:
```sh
pip install -r requirements.txt
```

### **3️⃣ Run the API Locally**
Start the FastAPI application with:
```sh
uvicorn main:app --reload
```

- The API will be accessible at: **http://127.0.0.1:8000/**

---
## 📌 API Documentation

### **Endpoint: Get Root Data**
- **URL:** `GET /`
- **Response Format:** JSON

#### **📌 Example Response**
```json
{
    "email": "muobotone@gmail.com",
    "current_datetime": "2024-01-29T14:30+00:00",
    "github_url": "https://github.com/runtmeyer/HNG_Task0"
}
```

---
## 🔗 Related Resource
Looking for expert **Python developers**? Check out:
[https://hng.tech/hire/python-developers](https://hng.tech/hire/python-developers)

---
**📌 Author:** [@runtmeyer](https://github.com/runtmeyer)

