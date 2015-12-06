<!DOCTYPE html>
<html>
<head>
<style>
table {
     border-collapse:collapse;
}
table, th, td {
     border: 2px solid black;
     font-family:arial;
     vertical-align:center;
     text-align:center;
     font-size:20pt;
}
body {
     background-color:#565A5C;
}
ul {
    list-style-type: none;
    margin: 0;
    padding: 0;
    overflow: hidden;
    border: 1px solid #e7e7e7;
    background-color: #A2A4A3;
    font-family:arial;
}

li {
    float: left;
}

li a {
    display: block;
    color: black;
    text-align: center;
    padding: 14px 16px;
    text-decoration: none;
}

li a:hover:not(.active) {
    color:white;
    background-color: #3f3f3f;
}

li a.active {
    color: black;
    background-color: #CFB87C;
}
</style>
</head>
<body>

<ul>
  <li><a href="home.php">Home</a></li>
  <li><a class="active" href="leaderboard.php">Leaderboard</a></li>
  <li><a href="doc.php">Other</a></li>
</ul>
<?php
$servername = "45.55.26.125:3306";
$username = "HTML";
$password = "website3308!";
$dbname = "Game_Data";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
     die("Connection failed: " . $conn->connect_error);
} 

$sql = "SELECT DISTINCT userName, scores FROM Scores ORDER BY scores";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
     echo "<table align='center' width='40%' cellpadding='3' cellspacing='3'><tr><th colspan='2' BGCOLOR='#CFB87C'><h2><br>The Big Bad Game</h3></th></tr>";
     echo "<tr><th BGCOLOR='#A2A4A3'>Player Name</th><th BGCOLOR='#A2A4A3'>Score</th></tr>";
     // output data of each row
     while($row = $result->fetch_assoc()) {
         echo "<tr><td BGCOLOR='#A2A4A3'>" . $row["userName"]. "</td><td BGCOLOR='#A2A4A3'>" . $row["scores"]. "</td></tr>";
     }
     echo "</table>";
} else {
     echo "0 results";
}

$conn->close();
?>  

</body>
</html>
