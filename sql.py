<?php
$conn = new mysqli("localhost", "root", "", "testdb");

$username = $_POST['username'];
$password = $_POST['password'];

// Use prepared statements to prevent SQL Injection
$stmt = $conn->prepare("SELECT * FROM users WHERE username = ? AND password = ?");
if (false === $stmt) {
    // Handle error, e.g., die('Prepare failed: ' . htmlspecialchars($conn->error));
}

$bind_success = $stmt->bind_param("ss", $username, $password); // 'ss' for two string parameters
if (false === $bind_success) {
    // Handle error, e.g., die('Bind failed: ' . htmlspecialchars($stmt->error));
}

$exec_success = $stmt->execute();
if (false === $exec_success) {
    // Handle error, e.g., die('Execute failed: ' . htmlspecialchars($stmt->error));
}

$result = $stmt->get_result();
// Process $result (e.g., fetch rows)
$stmt->close();

if ($result->num_rows > 0) {
    echo "Login başarılı";
} else {
    echo "Login başarısız";
}
?>

<form method="POST">
    <input type="text" name="username" placeholder="username">
    <input type="password" name="password" placeholder="password">
    <button type="submit">Login</button>
</form>