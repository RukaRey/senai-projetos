<?php
    include("php/db.php");
    $conn = createConn('localhost','root','','sistema_avaliacao');
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <form action="<?php htmlspecialchars($_SERVER['PHP_SELF']) ?>">

    </form>
</body>
</html>

<?php
    mysqli_close($conn);
?>