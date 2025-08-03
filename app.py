from flask import Flask, render_template, request, redirect, url_for, jsonify
import sqlite3


app = Flask(__name__)


# Database initialization
def init_db():
    conn = sqlite3.connect("todos.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS todos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            completed BOOLEAN DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """
    )
    conn.commit()
    conn.close()


@app.route("/")
def index():
    conn = sqlite3.connect("todos.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM todos ORDER BY created_at DESC")
    todos = cursor.fetchall()
    conn.close()
    return render_template("index.html", todos=todos)


@app.route("/add", methods=["POST"])
def add_todo():
    title = request.form["title"]
    description = request.form.get("description", "")

    conn = sqlite3.connect("todos.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO todos (title, description) VALUES (?, ?)", (title, description))
    conn.commit()
    conn.close()

    return redirect(url_for("index"))


@app.route("/toggle/<int:todo_id>")
def toggle_todo(todo_id):
    conn = sqlite3.connect("todos.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE todos SET completed = NOT completed WHERE id = ?", (todo_id,))
    conn.commit()
    conn.close()
    return redirect(url_for("index"))


@app.route("/delete/<int:todo_id>")
def delete_todo(todo_id):
    conn = sqlite3.connect("todos.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM todos WHERE id = ?", (todo_id,))
    conn.commit()
    conn.close()
    return redirect(url_for("index"))


@app.route("/api/todos")
def api_todos():
    conn = sqlite3.connect("todos.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM todos ORDER BY created_at DESC")
    todos = cursor.fetchall()
    conn.close()

    todos_list = []
    for todo in todos:
        todos_list.append(
            {
                "id": todo[0],
                "title": todo[1],
                "description": todo[2],
                "completed": bool(todo[3]),
                "created_at": todo[4],
            }
        )

    return jsonify(todos_list)


if __name__ == "__main__":
    init_db()
    app.run(debug=True, host="0.0.0.0", port=5000)
