<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>orderpage</title>
        <link href="css/styles.css" rel="stylesheet" />
    </head>
    <body>
		<nav class="navbar navbar-expand-lg navbar-light bg-light">
            <div class="container px-4 px-lg-5">
                <a class="navbar-brand" href="#!">Cart</a>
                <div class="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul class="navbar-nav me-auto mb-2 mb-lg-0 ms-lg-4">
                        <li class="nav-item"><a class="nav-link active" aria-current="page" href="http://stuweb.uic.edu.cn/q030026170/DBMS/shop.php">Shop</a></li>
                        <li class="nav-item"><a class="nav-link" href="http://stuweb.uic.edu.cn/q030026047/DBMS/cusInfo.php">About</a></li>
                    </ul>
                </div>
            </div>
        </nav>
	<header class="bg-dark py-5">
            <div class="container px-4 px-lg-5 my-5">
                <div class="text-center text-white">
                    <h1 class="display-4 fw-bolder">Orders in style</h1>
                    <p class="lead fw-normal text-white-50 mb-0">With this Cart template</p>
                </div>
            </div>
        </header>
<?php
include 'connectBC.php';
$cid = $_COOKIE["mycookie"];

$sql = "SELECT *FROM TEMP";
$result = mysqli_query($conn, $sql);
echo"<section class='py-5'>";
echo"<div class='container px-6 px-lg-7 mt-5'>";
echo"<div class='row gx-4 gx-lg-5 row-cols-4 row-cols-md-3 row-cols-xl-4 justify-content-center'><div class='col mb-5'><div class='card h-100'>";
echo"<div class='card-body p-4'><div class='text-center'><table>";

for($i=0;$i<$result->num_rows;$i++){
$row = mysqli_fetch_assoc($result);
$gname = $row['gname'];
$price = $row['price'];
echo"<tr><td><h5 class='fw-bolder'>".$gname."</td><td>￥".$price."</td></h5></tr>"; 
}
echo"</table></div></div></section>";

$sql = "INSERT INTO Orders(oid,cid,gid)
		SELECT oid, cid, gid
		FROM TEMP";
$result = mysqli_query($conn, $sql);
$sql = "TRUNCATE TABLE TEMP";
	$result = mysqli_query($conn, $sql);
?>

</html>