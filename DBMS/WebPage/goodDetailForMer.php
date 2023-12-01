<!DOCTYPE html>
<html lang="en" >
<head>
  <meta charset="UTF-8">
  <title> Product Page</title>
  <link rel="stylesheet" href="detailStyle.css">

</head>
<body>
<div class="container">
  <div class="header">
    <div class="header-logo">
      Product Page
    </div>
 </div>
 <?php

include 'conn.php';

 

//编写查询sql语句

$sql = 'SELECT * FROM Goods';

//执行查询操作、处理结果集

$result = mysqli_query($link, $sql);

if (!$result) {

    exit('查询sql语句执行失败。错误信息：'.mysqli_error($link));  // 获取错误信息

}

$data = mysqli_fetch_all($result, MYSQLI_ASSOC);

 

//编写查询数量sql语句

$sql = 'SELECT COUNT(*) FROM Goods';

//执行查询操作、处理结果集

$n = mysqli_query($link, $sql);

if (!$n) {

    exit('查询数量sql语句执行失败。错误信息：'.mysqli_error($link));  // 获取错误信息

}

$num = mysqli_fetch_assoc($n);

//将一维数组的值转换为一个字符串

$num = implode($num);

 

 

?>

       <h1>Goods Manage</h1>

       <div class="add">

           <a href="addStudent.html">Add goods</a>&nbsp;&nbsp;&nbsp;total<?php echo $num; ?>
       </div>

       <table width="960" border="1">

           <tr>

              <th>gid</th>

              <th>gname</th>

              <th>price</th>


           </tr>

           <?php

             

   

              foreach ($data as $key => $value) {

                  foreach ($value as $k => $v) {

                     $arr[$k] = $v;

                  }

              echo "<tr>";

              echo "<td>{$arr['gid']}</td>";

              echo "<td>{$arr['gname']}</td>";

              echo "<td>{$arr['price']}</td>";

              echo "<td>

                         <a href='javascript:del({$arr['gid']})'>delete</a>

                         <a href='addjust.php?id={$arr['gid']}'>adjust</a>

                    </td>";

              echo "</tr>";

              
			  }

              // 关闭连接

              mysqli_close($link);
			?>
</table>

</div>
 <script type="text/javascript">

       function del (id) {

           if (confirm("Are you sure to delete the good？")){

              window.location = "action_del.php?gid="+gid;

           }

       }

    </script>
</body>
</html>



 






    