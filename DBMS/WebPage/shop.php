<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Shop Homepage</title>
        <link href="css/styles.css" rel="stylesheet" />
    </head>
    <body>
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <div class="container px-4 px-lg-5" background = "url(image/123.jpg) no-repeat">
                <a class="navbar-brand" href="#!">Shop</a>
                <div class="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul class="navbar-nav me-auto mb-2 mb-lg-0 ms-lg-4">
                        <li class="nav-item"><a class="nav-link active" aria-current="page" href="#!">Home</a></li>
                        <li class="nav-item"><a class="nav-link" href="http://stuweb.uic.edu.cn/q030026047/DBMS/cusInfo.php">About</a></li>
                    </ul>
                    <form class="d-flex">
                        <button class="btn btn-outline-dark" type="submit">
                            <i class="bi-cart-fill me-1"></i>
                            <a href="http://stuweb.uic.edu.cn/q030026170/DBMS/orderpage.php" class="navbar-brand">Order</a>
                        </button>
                    </form>
                </div>
            </div>
        </nav>
		
        <header class="bg-dark py-5">
            <div class="container px-4 px-lg-5 my-5">
				<img src="image/123.jpg"  class="card-img-top"/>
                <div class="text-center text-white">
                    <h1 class="display-4 fw-bolder"></h1>
                    <p class="lead fw-normal text-white-50 mb-0">Shop in style</p>
                </div>
            </div>
        </header>
       
    </body>
<?php
include 'connectBC.php';

$sql = "SELECT *FROM Goods";
$result = mysqli_query($conn, $sql);
$cid = $_COOKIE["mycookie"];
$i = 0;
echo"<section class='py-5'><div class='container px-4 px-lg-5 mt-5'>
                <div class='row gx-4 gx-lg-5 row-cols-2 row-cols-md-3 row-cols-xl-4 justify-content-center'>";
while($i<10){
$i++;
$row = mysqli_fetch_assoc($result);
$gid = $row['gid'];
$gname = $row['gname'];
$price = $row['price'];
echo"<div class='col mb-5'>
        <div class='card h-100'>
            <img class='card-img-top' src='image/blankpicture.jpg' alt='...' />
                <div class='card-body p-4'>
                    <div class='text-center'>
                        <h5 class='fw-bolder'>".$gname."</h5>
                         ".$price."
                </div>
            </div>
                <div class='card-footer p-4 pt-0 border-top-0 bg-transparent'>
            <div class='text-center'><a class='btn btn-outline-dark mt-auto' href='http://stuweb.uic.edu.cn/q030026264/DBMS/goodDetailForCus.php?gid=$gid' >View details</a></div>
		</div>
        </div>
    </div>";
}
echo"</div></div></section>";
?>
</html>
