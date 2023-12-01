<html>
	<head>
	<title>Order page</title>
		<link rel="stylesheet" type="text/css" href="CssOfShopPHP.css" />
	</head>
	<body>
	<form>
		
	<?php
		$a = $_POST['QN1'];
		$b = $_POST['QN2'];
		$c = $_POST['QN3'];
		$d = $_POST['QN4'];
		$e = $_POST['QN5'];
		$f = $_POST['QN6'];
		$g = $_POST['QN7'];
		$h = $_POST['QN8'];
		
		$app = $_POST['Appellation'];
		$fn = $_POST['FN'];
		$ln = $_POST['LN'];
		$ac = $_POST['Account'];
		$pw = $_POST['PW'];
		$ad = $_POST['Address'];
				
		$qty = $a+$b+$c+$d+$e+$f+$g+$h;	
		$tp =  $a*48+$b*112+$c*38+$d*114+$e*36+$f*46+$g*39+$h*25;		
			
		echo "<div><h1>Transaction</h1>";
		echo "<h2>DATE: ".date('d M Y')."<h2><br>";
		$date = strtotime(date('d M Y'));
		echo "<h2>DELIVER DATE: ". date('d M Y',$date + 3*24*60*60)."</h2><br>";
		echo "<h2>CUSTOMER: ".$app." ".$fn." ".$ln."</h2><br>";
		echo "<h2>The goods will be shipped to Address:".$ad."</h2><br>";
		echo "<h2>Confirmation Order"."</h2><br>";
		echo "<table border=1>
		<tr bgcolor=#2c3e50 font-color=#ffffff>
			<th >NO</th>
			<th>Item Name</th>
			<th>Unit Price(RMB)</th>
			<th>Qty</th>
			<th>Total Price(RMB)</th>
		</tr>";
		$i = 0 ;
		if($a>0){
			echo
			"<tr>
			<td>".++$i."</td>
			<td>Lolita</td>
			<td>48</td>
			<td>".$a."</td>
			<td>".$a*48 ."</td>
			</tr>";
			}
	
		if($b>0){
			echo	
			"<tr>
			<td>".++$i."</td>
			<td>Liber Novus</td>
			<td>112</td>
			<td>".$b."</td>
			<td>".$b*112 ."</td>
			</tr>";
			}
		if($c>0){ 
			echo
			"<tr>
			<td>".++$i."</td>
			<td>Герой нашего времени</td>
			<td>38</td>
			<td>".$c."</td>
			<td>".$c*38 ."</td>
			</tr>";
			}
		if($d>0){
			echo				
			"<tr>
			<td>".++$i."</td>
			<td>The Crowd:A Study of the Popular Mind</td>
			<td>114</td>
			<td>".$d."</td>
			<td>".$d*114 ."</td>
			</tr>";
			}
		if($e>0){ 
			echo
			"<tr>
			<td>".++$i."</td>
			<td>The Journey to the West</td>
			<td>36</td>
			<td>".$e."</td>
			<td>".$e*36 ."</td>
			</tr>";
			}
		if($f>0){ 
			echo
			"<tr>
			<td>".++$i."</td>
			<td> Dream of the Red Chamber</td>
			<td>46</td>
			<td>".$e."</td>
			<td>".$e*46 ."</td>
			</tr>";
			}
		if($g>0){ 
			echo
			"<tr>
			<td>".++$i."</td>
			<td> The Story by the Water Margin</td>
			<td>39</td>
			<td>".$e."</td>
			<td>".$e*39 ."</td>
			</tr>";
			}
		if($h>0){ 
			echo
			"<tr>
			<td>".++$i."</td>
			<td > The Romance of the Three Kindoms</td>
			<td>25</td>
			<td>".$e."</td>
			<td>".$e*25 ."</td>
			</tr>";
			}
		echo
			"<tr>
			<td colspan = '3' align = 'left'>Finally Total</td>
			<td>" . $qty . "</td>
			<td>" . $tp . "</td>
			</tr></table></div>";
		
			
			
include 'connectBC.php';

$money = $tp;
$uname = $ac;
$pwd = $pw;

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
				echo "<div><h2> Your CustomerName is : $uname.<br>
				Your balance is not enough to withdrew $money RMB.</h2></div>";
				break;
			}
			else{
			$total  = $m_left - $money;
			$sql = "UPDATE BC SET RMB='$total' WHERE CustomerName ='$uname'";
			$result = $conn->query($sql);
			}
			if($result){
				echo "<div><h2>Your CustomerName is: $uname.<br>
					Your balance changes to $total RMB.<br>
					Thanks!</h2></div>";
			}
			else
				echo "<div><h2>Failed!</h2></div>";
		} else {
			echo "<div><h2>Your CustomerName $uname is not match the data base</h2></div>";
			break;
		}
	}
  }
} else {
  echo "<div><h2>0 results</h2></div>";
}
if(!$exist){
	echo "$uname does not exist";
}
$conn->close();

		
	?>
	</form>
	</body>
</html>
