<html>
<head>
<title>Transfer money</title>
</head>
<style>
body{
background-color:#2c3e50;
}
</style>
<body>
<link rel="stylesheet" href="bk.css">
<h1 id="s3">Transfer money page</h1>
<form action="tr.php" method="POST">
<p id="c"><input type="text" name="usr" value="" required />Your CustomerName</p>
<p id="c"><input type="password" name="pwd" value=""  required /> Password</p>
<p id="c"><input type="text" name="us" value="" required />Another CustomerName</p>
<p id="c"><input type="number" name="mon" value="" required />How much do you want to transfer(RMB)</p>
<input type="submit" value="Enter" /><br>
<a href=save.php id="here">CLICK HERE to save money</a><br>
<a href=with.php id="here">CLICK HERE to withdraw money</a><br>
<a href="Index.html" id="here">CLICK HERE back to Index</a>
</form>


</body>
</html>