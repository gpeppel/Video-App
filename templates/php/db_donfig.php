<?php 
$hostname = "myserver";
$username = "root";
$password = "password";
$database = "videoapp";

mysql_connect($hostname,$username,$password) or die ("connection failed");
mysql_select_db($database) or die ("error connect database");
?>