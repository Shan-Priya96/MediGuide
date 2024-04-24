<?php
// Database connection
$servername = "localhost";
$username = "root";
$password = "PASSWORD";
$dbname = "doc";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Process form submission
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = $_POST["name"];
    $location = $_POST["location"];
    $contact = $_POST["contact"];
    $timings = $_POST["timings"];
    $rating = $_POST["rating"];
    $specialisation = $_POST["specialisation"];

    // Insert data into database
    $sql = "INSERT INTO doctors (name, location, contact, timings, rating, specialisation)
            VALUES ('$name', '$location', '$contact', '$timings', '$rating', '$specialisation')";

    if ($conn->query($sql) === TRUE) {
        echo "New record created successfully";
    } else {
        echo "Error: " . $sql . "<br>" . $conn->error;
    }
}

// Close connection
$conn->close();
?>
