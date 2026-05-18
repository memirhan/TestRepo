const express = require("express");
const app = express();

// Helper function to escape HTML special characters
function escapeHtml(unsafe) {
  if (!unsafe) return '';
  return unsafe
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#039;");
}

app.get("/", (req, res) => {
  const name = req.query.name;
  // Escape the name before embedding it into HTML to prevent XSS
  const safeName = escapeHtml(name || 'Guest');

  res.send(`
    <h1>Merhaba ${safeName}</h1>
  `);
});

app.listen(3000);