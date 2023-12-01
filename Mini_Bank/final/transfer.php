<html>
	<head>
	<title>Convert Successfully</title>
		<link rel="stylesheet" type="text/css" href="CssForExPhp.css" />
	</head>
	<body>
	<h5><a id="link" href=Index.html>CLICK HERE </a>to back to the Index page.</h5>
<?php
include 'connectBC.php';

	$cname 	= $_POST["cn"];
	$pwd	= $_POST["pwd"];
	$money  = $_POST["rmb"];
	$cur    = $_POST["cur"];
	$ct = 0;
	$exist = false;
	$sql = "SELECT * FROM BC ";
	$result = $conn->query($sql);
    echo "<h4>You choose to convert $money RMB into $cur</h4><br>";
	if ($result->num_rows > 0) {
        while(($row = $result->fetch_assoc()) !== null) {
        if($cname == $row["CustomerName"]){
            $exist = true;
            if ($pwd == (int)$row["Passward"]){// password from db record
                    $mrmb = $row["RMB"]-$money;
                    $musd = $row["USD"];
                    $meur = $row["EUR"];
                    $mhkd = $row["HKD"];
                    if($cur=='USD'){
                        $ct = $musd+0.153*$money;
                        $sql = "UPDATE BC SET RMB='$mrmb', USD=".$ct." WHERE CustomerName='$cname'";
                        $result = $conn->query($sql);
                        if($result)
                            echo "<h4>Now you have $mrmb RMB, $ct USD.</h4> ";
                        else
                            echo "Failed!";
                    }
                    if($cur=='EUR'){
                        $ct = $meur+0.129*$money;
                        $sql = "UPDATE BC SET RMB='$mrmb', EUR=".$ct." WHERE CustomerName='$cname'";
                        $result = $conn->query($sql);
                        if($result)
                            echo "<h4>Now you have $mrmb RMB, $ct EUR.</h4> ";
                        else
                            echo "Failed!";
                    }
                    if($cur=='HKD'){
                        $ct = $mhkd+1.188*$money;
                        $sql = "UPDATE BC SET RMB='$mrmb', HKD=".$ct." WHERE CustomerName='$cname'";
                        $result = $conn->query($sql);
                        if($result)
                            echo "<h4>Now you have $mrmb RMB, $ct HKD.</h4> ";
                        else
                            echo "Failed!";
                    }

            } else {
                echo "Your Customer name $cname is not match the data base";
                break;
            }
        }
      }
}
  else {
  echo "0 results";
}
if(!$exist){
	echo "$cname does not exist";
}
$conn->close();

?>
	</body>
</html>