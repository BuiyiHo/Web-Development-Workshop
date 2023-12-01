<!DOCTYPE html>
<html>
<head>
	<title>Login Page</title>
	<link type="text/css" rel="styleSheet"  href="Login.css" />
</head>
<body>
	<div class="wai">
		<br>
		<h1 class="center1">Weclome</h1>

		<div class="login">
			<p class="register">LOGIN</p>
	
			<form action="" method="post">
			<input name="Username" onClick = "bkgColor(this)" onBlur="bkgWhite(this)" class="inbox" required='required' placeholder="UserID" /><br/>
			<input name="Password" type = "password"onClick = "bkgColor(this)" onBlur="bkgWhite(this)" class="inbox" required='required' placeholder="Password" />
			<br /><br />
			<select style=" margin-left:110px" name="Role">
			<option value="Customer" selected>Customer</option>
			<option value="Merchant">Merchant</option>
			</select>
			<br/><br/>
			<input  style=" margin-left:130px" type="submit" >
			<br />
			<p class="link">Don't have account?
			<a href='http://stuweb.uic.edu.cn/q030026229/DBMS/Register.php' class='button' >Sign up</a>
			</p>
			</form>
		</div>
	</div>

	<?php
		//connect the database
		$servername = "localhost";	
		$username = "2030026065"; 
		$password ="2030026065";
		$db = "2030026065";
		$conn = new mysqli($servername, $username, $password, $db);
  		$u = $_POST["Username"];
  		$p = $_POST["Password"];
  		$r = $_POST["Role"];
  		if($r == "Customer"){
  		$confirmU=" SELECT * FROM Customer WHERE cid = $u ";
  		$result = mysqli_query($conn, $confirmU);
  		$row = mysqli_fetch_assoc($result);//get the information from the database based on the input name
  		$forPage=null;
		if($row["cid"] == null){
			if($row["passward"] != $p){//determine whether the username and password are correct
			echo "<script>alert('Sorry, your username and password are incorrect!')</script>";
			}	
		}
		else if($row["cid"] != null){
			if($row["passward"] != $p){//determine whether the password is correct
			echo "<script>alert('Sorry, your password is incorrect!')</script>";}
			else{
				setcookie('check',true);
				setcookie('myCid',$u);
				echo"<script type='text/javascript'>";
				$url = "http://stuweb.uic.edu.cn/q030026170/DBMS/shop.php";
				echo"
					alert('You successfully log in!');
					window.location.href = '$url';
					</script>";
			}
		}
	}
 
 		if($r == "Merchant"){
  		$confirmU=" SELECT * FROM Merchant WHERE mid = $u ";
  		$result = mysqli_query($conn, $confirmU);
  		$row = mysqli_fetch_assoc($result);//get the information from the database based on the input name
  		$forPage=null;
		if($row["mid"] == null){
			if($row["passward"] != $p){//determine whether the username and password are correct
			echo "<script>alert('Sorry, your username and password are incorrect!')</script>";
			}	
		}
		else if($row["mid"] != null){
			if($row["passward"] != $p){//determine whether the password is correct
			echo "<script>alert('Sorry, your password is incorrect!')</script>";}
			else{
				setcookie('check',true);
				setcookie('myMid',$u);
				echo"<script type='text/javascript'>";
				$url = "merInfo.php";
				echo"
					alert('You successfully log in!');
					window.location.href = '$url';
					</script>";
			}
		}
	}
		if (mysqli_query($conn, $sql)) {
			}
		else {
    		//echo $sql . "<br>" . mysqli_error($conn);
		}
		mysqli_close($conn);
	?>

	<?php
	//change the backgroundColor of the input field
	echo "<script type='text/javascript'>
	function bkgColor(a){
		a.style.backgroundColor='#FFCCCC';
	}
	</script>";
	echo"<script type='text/javascript'>
	function bkgWhite(a){
		a.style.backgroundColor='#FFFFFF';
	}
	</script>";
?>


</body>
</html>


