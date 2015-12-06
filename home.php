<!DOCTYPE html>
<html>
<head>
<style>
body {
     background-color:#565A5C;
     font-family:arial;
}
p{
    color:white;
    font-size:20pt;
    
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
  <li><a class="active" href="home.php">Home</a></li>
  <li><a href="leaderboard.php">Leaderboard</a></li>
  <li><a href="doc.php">Other</a></li>
</ul>
<p>Welcome to the home of the Big Bad Game! A pygame made for CSCI 3308 at CU-Boulder.</p>
<p>The tabs above navigate you around the website. Leaderboard takes you to the current leaderboard for the game itself, see where you rank among your friends!</p>
</body>
</html>
