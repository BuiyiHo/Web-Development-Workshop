<html>
<style>
body{
background-color:white;
}
</style>
<body>
<link rel="stylesheet" href="mer&cus.css">
<h1 class="mer">Your goods<br></h1>	
</body>


<?php
$MID = $_COOKIE["myMid"];
include 'connectBC.php';

//$MID = $_POST["mID"];


$exist = false;
$sql = "SELECT *FROM Provide, Goods, Merchant WHERE Goods.gid = Provide.gid and Provide.mid = Merchant.mid";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
  // output data of each row
  while($row = $result->fetch_assoc()) {
	if($MID == $row["mid"]){
		$exist = true;
			$Gname = $row["gname"];
			echo "$Gname.";
	}
  }
} else {
  echo "0 results";
}
if(!$exist){
	echo "$MID does not exist";
}
$conn->close();

?>
<h3><a href="http://stuweb.uic.edu.cn/q030026047/DBMS/merInfo.php" id="here">CLICK HERE to go back</a></h3>
</html>