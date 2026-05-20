import mysql from "mysql2/promise";

const db = await mysql.createConnection({
  host: process.env.DB_HOST || "localhost",
  user: process.env.DB_USER,
  password: process.env.DB_PASSWORD,
  database: process.env.DB_NAME
});

const username = process.env.APP_USERNAME || "admin";
const password = process.env.APP_PASSWORD || "1234";

// SAFE: SQL injection engellenmiş
const [rows] = await db.execute(
  "SELECT * FROM users WHERE username = ? AND password = ?",
  [username, password]
);

console.log(rows);