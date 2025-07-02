<?php
$conn = new mysqli("localhost", "vulnuser", "vulnpass", "vulnsite");
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Use POST instead of GET
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $user = $_POST['username'];
    $pass = $_POST['password'];

    $sql = "SELECT * FROM users WHERE username = '$user' AND password = '$pass'";
    $result = $conn->query($sql);

    if ($result->num_rows > 0) {
        header("Location: dashboard.php");
        exit();
    } else {
        echo "<p style='color:red;'>Login failed. Invalid credentials.</p>";
    }
}
?>

<!-- Login Form -->
<h2>Login to Your Account</h2>
<form method="POST">
    <label>Username:</label><br>
    <input type="text" name="username" required><br><br>
    <label>Password:</label><br>
    <input type="password" name="password" required><br><br>
    <input type="submit" value="Login">
</form>

<!-- Optional: Link to upload page -->
<p><a href="upload.php">Upload Documents</a></p>
