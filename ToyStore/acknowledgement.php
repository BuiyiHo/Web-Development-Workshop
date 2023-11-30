<?php
    if(!isset($_POST['list'])){
        echo "empty cart";
        exit();
    }
?>

<html>
<head><title>Toys House</title>
<link rel="stylesheet" href="index.css">
</head>
<body>
<fieldset><legend>CUSTOM INFO</legend>
    <div><h2><?php echo $_POST["call"]." ".$_POST["firstname"]." ".$_POST["familyname"]; ?></h2></div>
    <br>
    <div><h2><?php echo "Address: ".$_POST["address"].", ".$_POST["province"]; ?></h2></div>
    <br>
    <div><h2><?php echo "Phone Number: ".$_POST["phonenumber"]; ?></h2></div>
</fieldset>

<fieldset><legend>LIST</legend>
    <table style="border: 1px solid black">
        <tr><td>No</td><td>Item Name</td><td>Unit Price($)</td><td>Qty</td><td>Total Price($)</td></tr>
        <?php
            $counter = 1;
            $overalltotal = 0;
            $overallqty = 0;
            foreach (json_decode($_POST["list"]) as $i){
                $overalltotal+=$i->total;
                $overallqty+=$i->qty;
                echo "<tr><td>".$counter++."</td><td>$i->name</td><td>$i->price</td><td>$i->qty</td><td>$i->total</td></tr>";
            }
            echo "<tr><td colspan='3'>Overall Total</td><td>$overallqty</td><td>$overalltotal</td></tr>";
        ?>

    </table>
</fieldset>
</body>
</html>

