from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)


def get_db():
    conn = sqlite3.connect("todo.db")
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            done INTEGER DEFAULT 0
        )
    """)

    conn.commit()
    conn.close()


@app.route("/")
def index():
    conn = get_db()

    tasks = conn.execute(
        "SELECT * FROM tasks ORDER BY id DESC"
    ).fetchall()

    conn.close()

    return render_template("index.html", tasks=tasks)


@app.route("/add", methods=["POST"])
def add_task():
    title = request.form["title"]

    conn = get_db()

    conn.execute(
        "INSERT INTO tasks (title) VALUES (?)",
        (title,)
    )

    conn.commit()
    conn.close()

    return redirect("/")


@app.route("/done/<int:task_id>")
def done_task(task_id):
    conn = get_db()

    conn.execute(
        "UPDATE tasks SET done = 1 WHERE id = ?",
        (task_id,)
    )

    conn.commit()
    conn.close()

    return redirect("/")


@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    conn = get_db()

    conn.execute(
        "DELETE FROM tasks WHERE id = ?",
        (task_id,)
    )

    conn.commit()
    conn.close()

    return redirect("/")


if __name__ == "__main__":
    init_db()

    app.run(
        host="0.0.0.0",
        port=5000
    )