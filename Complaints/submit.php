<?php
$user_name = $_POST['user_name'];
$user_email = $_POST['user_email'];
$complaint_text = $_POST['complaint_text'];
$category = $_POST['category'];

$host = null;
$dbUsername = null;
$dbPassword = "*pjV9^=7nFIE9esp=}L]";
$dbName = "complaints";
$conn = new mysqli('your_host', 'your_username', 'your_password', 'your_database');
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Insert complaint details into the database
$sql = "INSERT INTO complaints (user_name, user_email, complaint_text, category) VALUES ('$user_name', '$user_email', '$complaint_text', '$category')";
if ($conn->query($sql) === TRUE) {
    echo "Complaint submitted successfully";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();
?>
