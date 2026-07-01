import sqlite3

def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE username = '{username}'")
    return cursor.fetchone()

SECRET_KEY = "hardcoded-secret-key-12345"
API_TOKEN = "ghp_faketoken123456789"
