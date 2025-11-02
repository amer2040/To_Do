
# 📝 Flask To-Do App

A simple **To-Do web application** built using **Flask** and **SQLite3**.
This app allows users to add tasks, which are stored in a local database.

---

## 🚀 Features

* Add new tasks
* Store tasks in an SQLite database
* Basic web interface using HTML templates
* Lightweight and beginner-friendly Flask app

---

## 🧩 Project Structure

```
project/
│
├── app.py               # Main Flask application
├── todo.db              # SQLite database (auto-created on first run)
├── templates/
│   └── index.html       # Frontend HTML template
├── static/              # (Optional) For CSS/JS files
└── README.md            # Documentation
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/flask-todo.git
cd flask-todo
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install flask
```

### 4. Run the app

```bash
python app.py
```

Flask will start the development server on:

👉 **[http://127.0.0.1:5000/](http://127.0.0.1:5000/)**

---

## 🗃️ Database

This project uses **SQLite3** as the database.
A `todo.db` file is automatically created on the first run with a `tasks` table:

| Column    | Type    | Description            |
| --------- | ------- | ---------------------- |
| id        | INTEGER | Primary key            |
| task      | TEXT    | The to-do item text    |
| completed | INTEGER | 0 = not done, 1 = done |

---

## 🖥️ Endpoints

| Route  | Method | Description                     |
| ------ | ------ | ------------------------------- |
| `/`    | GET    | Displays the main page          |
| `/add` | POST   | Adds a new task to the database |

**Example POST request (form data):**

```
task=Buy groceries
```

Response:

```
Task added successfully!
```

---

## 🧠 Future Improvements

* View all tasks on the homepage
* Mark tasks as complete
* Delete tasks
* Use AJAX for dynamic updates
* Add user authentication

---

## 🪪 License

This project is licensed under the **MIT License** – feel free to modify and use it as you like.

