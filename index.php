import sqlite3
import bcrypt

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

username = input("Username: ")
password = input("Password: ")

cursor.execute("SELECT password_hash FROM users WHERE username=?", (username,))
result = cursor.fetchone()

if result:
    stored_hashed_password = result[0].encode('utf-8')
    if bcrypt.checkpw(password.encode('utf-8'), stored_hashed_password):
        print("Login successful")
    else:
        print("Invalid credentials")
else:
    print("Invalid credentials")