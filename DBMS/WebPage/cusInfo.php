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
	$exist=false;
	$sql = "SELECT *FROM Customer WHERE cid = $cid";
	$result = mysqli_query($conn, $sql);
	while($row = mysqli_fetch_assoc($result)){	
		if($cid=$row["cid"]){
			$exist=true;
			$name=$row["cname"];
			$city=$row["city"];
			$address=$row["address"];
		}
		$conn->close();
	}
	echo"<h5>Customer's Name:$name</h5><h5>City:$city</h5><h5>Address:$address</h5>";	
?>
			</div>
		</div>
		<div class="links">
			<ul >
				<li ><a  href="Login.php">Login</a></li>
				<li ><a  href="http://stuweb.uic.edu.cn/q030026170/DBMS/shop.php">Goods</a></li>
				<li ><a  href="cu.php">History Order</a></li>
			</ul>
		</div>
	</div>

	<section class="half-parallax">
		<div class="parallax-items">
			<div class="container">
				<div class="col-lg-4 col-md-6 col-sm-12">
					<div class="parallax-item">
						<i class="fa fa-hourglass-o"></i>
						<h5 class="feature-title">Change Name</h5>
						<p>Please input your new name</p>
						<form method="POST" action="changeInfocus.php?action=changeName">
							<input type="text" name="newName">
							<input type="submit" ><br>
						</form>
					</div>
				</div>
				
				<div class="col-lg-4 col-md-6 col-sm-12">
					<div class="parallax-item">
						<i class="fa fa-connectdevelop"></i>
						<h5 class="feature-title">Set Password</h5>
						<p>Please input your new password</p>
						<form method="POST" action="changeInfocus.php?action=changePw">
							<input type="text" name="newPassword">
							<input type="submit" ><br>
						</form>
					</div>
				</div>
				<div class="col-lg-4 col-md-6 col-sm-12">
					<div class="parallax-item">
						<i class="fa fa-flag-o"></i>
						<h5 class="feature-title">Deactivate</h5>
						<p>If you want to deactivate your account please click here</p>	
						<form method="POST" action="changeInfocus.php?action=deac">
							<input type="submit" ><br>
						</form>
						</a>
					</div>
				</div>
			</div>
		</div>
	</section>
</body>
</html>
