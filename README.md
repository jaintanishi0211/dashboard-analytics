# Analytics Dashboard (FastAPI + Chart.js)

## Project Overview

This project visualizes key productivity metrics using a FastAPI backend and a lightweight frontend.

It provides real-time insights such as:

* Total Users
* Active Users
* Tasks Completed
* Efficiency Rate

The frontend consumes REST APIs and renders interactive charts.

---

## Tech Stack

### Backend

* FastAPI (Python)
* Uvicorn

### Frontend

* HTML, CSS, JavaScript
* Chart.js (for data visualization)

### Deployment

* Backend: Render
* Frontend: Vercel

---

## Project Structure

```
dashboard_analytics/
│
├── backend/
│   ├── main.py
│   ├── routes/
│   │   └── stats.py
│   ├── services/
│   │   └── analytics.py
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   ├── script.js
```

---

## Features

* REST API using FastAPI
* Modular backend (routes + service layer)
* Dynamic frontend using fetch API
* Two interactive charts:

  * Doughnut chart (Task Distribution)
  * Line chart (User Growth)
* Clean and responsive UI

---

## API Endpoint

### GET `/api/stats`

Returns:

```json
{
  "total_users": 1543,
  "active_users": 1109,
  "completed_tasks": 670,
  "pending_tasks": 562,
  "efficiency": 54.39,
  "tasks_chart": {
    "labels": ["Completed", "Pending"],
    "data": [670, 562]
  },
  "users_chart": {
    "labels": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "values": [200, 340, 500, 800, 1200, 1543]
  }
}
```

---

## How to Run Locally

### 1. Clone the repository

```
git clone https://github.com/jaintanishi0211/dashboard-analytics.git
cd dashboard-analytics
```

---

### 2. Run Backend

```
cd backend
pip install fastapi uvicorn
uvicorn main:app --reload
```

Backend runs at:

```
http://127.0.0.1:8000
```

---

### 3. Run Frontend

Open a new terminal:

```
cd frontend
python -m http.server 5500
```

Open in browser:

```
http://127.0.0.1:5500
```

---

## Deployment

### Backend (Render)

* Deploy FastAPI backend
* Start command:

```
uvicorn main:app --host 0.0.0.0 --port 10000
```

---

### Frontend (Vercel)

* Set root directory to `frontend`
* Update API URL in `script.js` to deployed backend URL

---

## 🎯 Key Learnings

* Building REST APIs with FastAPI
* Structuring backend using service layer
* Integrating frontend with APIs
* Data visualization using Chart.js
* Deploying full-stack applications

---
