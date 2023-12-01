<?php
	

	$servername="localhost";
	$username="2030026170";
	$password="2030026170";
	$db="2030026170";

	//create connection
	$conn= new mysqli($servername,$username,$password,$db);
	
	//check connection
	if ($conn->connect_error){
		die("<h2>connection failed: </h2>".$conn->connect_error);
	}
	return ($conn);
	
	
?>
