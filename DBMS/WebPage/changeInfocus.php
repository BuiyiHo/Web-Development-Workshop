<?php
$cid=$_COOKIE["myCid"];
include "connectBC.php";
?>
<html>
<head>
	<link href="Info.css" rel="stylesheet" type="text/css">
</head>
<body>
	<div class="welcome">
		<div class="welcome-content">
			<div class="welcome-text">
				<h1>Customer's Information</h1>
				<?php
					if($_REQUEST['action']=='changeName'){
						$name=$_POST['newName'];
						$sql = "UPDATE Customer SET cname='$name' WHERE cid=$cid";
						$result=mysqli_query($conn,$sql);
						if($result) {
							echo  "Success: Your new name is ".$name;
							}
						else{
							echo "Error updating record";
						}
						mysqli_close($conn);
					}
					if($_REQUEST['action']=='changePw'){
						$pw=$_POST['newPassword'];
						$sql = "UPDATE Customer SET passward='$pw' WHERE cid=$cid";
						$result=mysqli_query($conn,$sql);
						if($result) {
							echo  "Success: Your new Password is ".$pw;
							}
						else{
							echo "Error updating record";
						}
						mysqli_close($conn);
					}
					if($_REQUEST['action']=='deac'){
						$sql = "DELETE FROM Customer WHERE cid=$cid";
						$result = mysqli_query($conn, $sql);
						echo  "Success: Your account has been deactivated ";
						mysqli_close($conn);
					}
				?>
			</div>
		</div>
		<div class="links">
			<ul >
				<li ><a  href="Login.php">Login</a></li>
				<li ><a  href="http://stuweb.uic.edu.cn/q030026170/DBMS/shop.php">Goods</a></li>
				<li ><a  href="cu.php">History Order</a></li>
				<li ><a  href="http://stuweb.uic.edu.cn/q030026047/DBMS/cusInfo.php">Back to Information</a></li>
			</ul>
		</div>
	</div>
</body>
</html>