<?php
$host = null;
$dbUsername = null;
$dbPassword = "";
$dbName = "complaints";
$conn = new mysqli($host, $dbUsername, $dbPassword, $dbName);
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Retrieve complaints from the database
$sql = "SELECT * FROM complaints";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // Display complaints in a table or list format
    echo "<h2>Complaints</h2>";
    echo "<table>";
    echo "<tr><th>Name</th><th>Email</th><th>Complaint</th><th>Category</th></tr>";

    while ($row = $result->fetch_assoc()) {
        echo "<tr>";
        echo "<td>".$row['user_name']."</td>";
        echo "<td>".$row['user_email']."</td>";
        echo "<td>".$row['complaint_text']."</td>";
        echo "<td>".$row['category']."</td>";
        echo "</tr>";
    }

    echo "</table";
}else{
    echo "No complaints found";
}

$conn->close();
?>