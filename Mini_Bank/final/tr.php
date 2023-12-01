<html>
<style>
body{
background-color:#2F4F4F;
}
</style>
<body>
<a href="Index.html" id="here">CLICK HERE back to Index</a>
</body>
</html>

<?php

include 'connectBC.php';

$uname 	= $_POST["usr"];
$pwd	= $_POST["pwd"];
$money  = $_POST["mon"];
$aname 	= $_POST["us"];

$exist = false;
$sql = "SELECT *FROM BC";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
  // output data of each row
  while($row = $result->fetch_assoc()) {
	if($uname == $row["CustomerName"]){
		$exist = true;
		if ($pwd == $row["Passward"]){
			// password from bc record
			$m_left = $row["RMB"];
			if($money > $m_left){
				echo " Your CustomerName is : $uname.<br>
				Your balance is not enough to withdrew $money RMB.";
				break;
			}
			else{
			$total  = $m_left - $money;
			$sql = "UPDATE BC SET RMB='$total' WHERE CustomerName ='$uname'";
			$result = $conn->query($sql);
			}
			if($result)
				echo "Your CustomerName is: $uname.<br>
			Your balance changes to $total RMB.";
			else
				echo "Failed!";
		} else {
			echo "Your CustomerName $uname is not match the data base";
			break;
		}
	}
  }
} else {
  echo "0 results";
}
if(!$exist){
	echo "$uname does not exist";
}

$exist = false;
$sql = "SELECT *FROM BC";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
  // output data of each row
  while($row = $result->fetch_assoc()) {
	if($aname == $row["CustomerName"]){
		$exist = true;
		//if ($pwd == $row["Passward"]){
			// password from bc record
			$m_leftt = $row["RMB"];
			$totall  = $money + $m_leftt;
			$sql = "UPDATE BC SET RMB='$totall' WHERE CustomerName ='$aname'";
			$result = $conn->query($sql);
			if($result)
				echo "Your CustomerName is: $aname.<br>
			Your balance changes to $totall RMB.";
			else
				echo "Failed!";
		
			break;
		}
	}
  }

	else {
	  echo "0 results";
	}
	if(!$exist){
		echo "$aname does not exist";
	}
$conn->close();
?>


