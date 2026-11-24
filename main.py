from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3 as sq

app = FastAPI()

def create_table():
    conn = sq.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        password TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()


def save_info(username, email, password):
    conn = sq.connect("users.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
        (username, email, password)
    )

    conn.commit()
    conn.close()


class User(BaseModel):
    username: str
    email: str
    password: str


create_table()


@app.get("/")
def home():
    return {"message": "Merhaba"}


@app.get("/users")
def users():
    conn = sq.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("SELECT username FROM users")
    rows = cursor.fetchall()

    conn.close()

    return rows


@app.post("/register")
def register(user: User):
    save_info(user.username, user.email, user.password)