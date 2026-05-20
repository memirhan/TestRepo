import mysql from "mysql2/promise";

const db = await mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "password",
  database: "testdb"
});

const username = "admin";
const password = "1234";

// SAFE: SQL injection engellenmiş
const [rows] = await db.execute(
  "SELECT * FROM users WHERE username = ? AND password = ?",
  [username, password]
);

console.log(rows);
