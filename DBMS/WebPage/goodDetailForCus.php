<!DOCTYPE html>
<html lang="en" >
<head>
  <meta charset="UTF-8">
  <title> Product Page</title>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/meyer-reset/2.0/reset.min.css">
<link rel='stylesheet' href='https://code.ionicframework.com/ionicons/2.0.1/css/ionicons.min.css'><link rel="stylesheet" href="detailStyle.css">

</head>
<body>
<div class="container">
  <div class="header">
    <div class="header-logo">
      Product Page
    </div>
    <nav class="header-nav">
	  <a href="http://stuweb.uic.edu.cn/q030026170/DBMS/orderpage.php">
      <i class="ion-ios-cart"></i>
      </a>
      <a href="http://stuweb.uic.edu.cn/q030026170/DBMS/shop.php">
	  <div></div>
      </a>
    </nav>
  </div>
  <div class="product">
    <div class="product-photo">
      <img src="image/suit1.jpg">
      <img src="image/suit2.jpg">
    </div>
    <div class="product-detail">
      
      
<?php 
include 'connectBC.php';
$cid = $_COOKIE['mycookie'];
$gid = $_GET['gid'];
$sql1 = "SELECT *FROM Goods where gid=$gid";
$query =  mysqli_query($conn,$sql1);
$row =  mysqli_fetch_assoc($query);
$name = $row["gname"];
$price = $row["price"];
echo "<h1 class='product__title'>$name</h1>
      <div class='product__price'>￥$price</div>";
?>
 <div class='product__subtitl'>Neat appearance, smooth lines and comfortable wearing. If you wear a tie, it will look more elegant and classic</div>
      <div class='product__color'>
        <form action=''>
          <fieldset>
            <input type='radio' name='color'>
            <label for='straw'>
              <i class='ion-android-done'></i>
            </label>
          </fieldset>
          <fieldset>
            <input type='radio' name='color'>
            <label for='brown'>
              <i class='ion-android-done'></i>
            </label>
          </fieldset>
        </form>
      </div>
	  <form method='post' onClick='buttonAnimate()'>
	  <button class='product__button' type='submit' value='Update' name='update'>Add to cart</button>
      </form>
    </div>
  </div>
 <?php
	include 'connectBC.php';
	$gid = $_GET['gid'];
	$up = $_POST['update'];
	if($up == "Update"){
	$sql2 = "INSERT INTO TEMP(gid) VALUES($gid)";
	$result =   mysqli_query($conn,$sql2);
		if($result){
		echo"<script type='text/javascript'>";
		echo"window.location.href = 'http://stuweb.uic.edu.cn/q030026170/DBMS/shop.php';</script>";
	}}
 ?>
</div>
  <script  src="goodDetailscript.js"></script>

</body>
</html>
