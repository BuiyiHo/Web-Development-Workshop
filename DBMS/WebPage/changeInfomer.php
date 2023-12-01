<?php
$mid=$_COOKIE["myMid"];
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
				<h1>Merchant's Information</h1>
				<?php
					if($_REQUEST['action']=='changeName'){
						$name=$_POST['newName'];
						$sql = "UPDATE Merchant SET cname='$name' WHERE mid=$mid";
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
						$sql = "UPDATE Merchant SET passward='$pw' WHERE mid=$mid";
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
						$sql = "DELETE FROM Merchant WHERE mid=$mid";
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
				<li ><a  href="me.php">Merchandise</a></li>
				<li ><a  href="http://stuweb.uic.edu.cn/q030026047/DBMS/merInfo.php">Back to Information</a></li>	
			</ul>
		</div>
	</div>
</body>
</html>