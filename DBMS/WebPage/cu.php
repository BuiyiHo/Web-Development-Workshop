<html>
<style>
body{
background-color:white;
}
</style>
<body>
<link rel="stylesheet" href="mer&cus.css">
<h1 class="cus">Your order<br></h1>
</body>


<?php
$CID = $_COOKIE["myCid"];
include 'connectBC.php';


//$pas = $_POST["pwd"];

$exist = false;
$sql = "SELECT *FROM Orders, Goods WHERE Orders.gid = Goods.gid";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
  // output data of each row
  while($row = $result->fetch_assoc()) {
	if($CID == $row["cid"]){
		$exist = true;
			$Oid = $row["oid"];
			$Gname = $row["gname"];
			echo "Order ID: $Oid<br>
			      Goods name: $Gname";
			
	}
  }
} else {
  echo "0 results";
}
if(!$exist){
	echo "$CID does not exist";
}
$conn->close();

?>
<a href="http://stuweb.uic.edu.cn/q030026047/DBMS/cusInfo.php"id="here">CLICK HERE to go back</a>
</html>