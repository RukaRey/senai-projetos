<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <form action="<?php htmlspecialchars($_SERVER['PHP_SELF']); ?>" method="post">
        <p>Clique em "Enviar" para concluir</p>
        <input type="submit" name="back">
    </form>
</body>
</html>

<?php 
    if(isset($_POST['back'])){
        header('Location: ../index.php');
    }
?>