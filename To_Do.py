from flask import Flask, render_template, request
import sqlite3

app = Flask("To_Do")

# Create a SQLite database
conn = sqlite3.connect('todo.db')
c = conn.cursor()

# Create a SQLite database and a table for storing tasks
def init_db():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY,
                    task TEXT,
                    completed INTEGER DEFAULT 0
                )""")
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form['task']

    # Open a new connection and add the task to the database
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
    conn.commit()
    conn.close()
    return 'Task added successfully!'

if __name__ == '__main__':
    init_db()
    app.run(debug=True)