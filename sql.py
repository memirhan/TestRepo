<?php
$conn = new mysqli("localhost", "root", "", "testdb");

$username = $_POST['username'];
$password = $_POST['password'];

$stmt = $conn->prepare("SELECT * FROM users WHERE username = ? AND password = ?");

if (!$stmt) {
    // Handle error appropriately, e.g., log it and display a generic message.
    // For debugging, you might use: die('MySQL prepare error: ' . $conn->error);
    // To preserve original logic flow, if prepare fails, assume no rows found or an error occurred leading to login failure.
    // Set $result to an object that will make num_rows > 0 false
    $result = (object) ['num_rows' => 0];
} else {
    $stmt->bind_param("ss", $username, $password); // 'ss' specifies that both parameters are strings
    $stmt->execute();
    $result = $stmt->get_result();
}

if ($result->num_rows > 0) {
    echo "Login başarılı";
} else {
    echo "Login başarısız";
}

// Close the statement if it was successfully prepared
if (isset($stmt) && $stmt !== false) {
    $stmt->close();
}
?>

<form method="POST">
    <input type="text" name="username" placeholder="username">
    <input type="password" name="password" placeholder="password">
    <button type="submit">Login</button>
</form>