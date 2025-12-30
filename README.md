# 📝 Task Manager Web Application (Flask)

A simple task management web application built using **Flask**.  
This project allows users to **add tasks, mark them as completed, and delete tasks** through a clean and minimal interface.

> ⚠️ Note: This README documents the project **only up to Step 5** (core features). No advanced refactoring or database persistence is included here.

---

## 🚀 Features (Up to Step 5)

- ➕ Add new tasks
- 📋 View all tasks
- ✅ Mark tasks as completed
- ❌ Delete tasks
- 🧠 Simple in-memory task storage
- 🖥️ Server-side rendering using Flask templates

---

## 🛠️ Tech Stack

- **Backend:** Flask (Python)
- **Frontend:** HTML (Jinja2 Templates)
- **Styling:** Basic CSS
- **Storage:** In-memory Python list



## 📁 Project Structure (Up to Step 5)

text
task_manager/
│
├── app.py
├── requirements.txt
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── README.md

## ⚙️ Setup Instructions
### 1️⃣ Clone the Repository
``` bash
git clone <your-repo-url>
cd task_manager
```
### 2️⃣ Create Virtual Environment
```bash
python -m venv venv
```
Activate it 
```bash
venv\Scripts\activate
```
### 3️⃣ Install Dependencies
```bash
pip install flask
pip freeze > requirements.txt
```
Run the application
```bash
python app.py
```
open the flash server(local host)
## 📌 How the App Works (Step 5 Scope)
Tasks are stored temporarily in a Python list
Each task has:
- a unique ID
- a task name
- a completion status
Routes handle:
- adding tasks
- marking tasks as completed
- deleting tasks
UI is rendered using Jinja2 templates
## ⚠️ Limitations 
- Tasks are not persisted
- Restarting the server clears all tasks
- No authentication or database integration
