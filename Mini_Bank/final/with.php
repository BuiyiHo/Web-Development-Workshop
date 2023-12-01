<html>
<head>
<title>Withdraw money</title>
</head>
<style>
body{
background-color:#2c3e50;
}
</style>
<body>
<link rel="stylesheet" href="bk.css">
<h1 id="s2">Withdraw money page</h1>
<form action="wi.php" method="POST">
<p id="c"><input type="text" name="usr" value="" required />CustomerName</p>
<p id="c"><input type="password" name="pwd" value=""  required /> Password</p>
<p id="c"><input type="number" name="mon" value="" required />How much do you want to withdraw(RMB)</p>
<input type="submit" value="Enter" /><br>
<a href=save.php id="here">CLICK HERE to save money</a><br>
<a href=tran.php id="here">CLICK HERE to transfer money</a><br>
<a href="Index.html" id="here">CLICK HERE back to Index</a>
</form>


</body>
</html>