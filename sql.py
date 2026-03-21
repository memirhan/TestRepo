import sqlite3

conn = sqlite3.connect("userss.db")
cursor = conn.cursor()

username = input("Username: ")
password = input("Password: ")

cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))

user = cursor.fetchone()

if user:
    print("Login successful")
else:
    print("Invalid credentials")
