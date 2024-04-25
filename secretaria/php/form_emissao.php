<?php
    include('../php/db.php');
    session_start();
    $conn = createConn('localhost','root','','db_secretaria');
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <div>
        <p>Solicitação de emissão de documentos escolares</p>
        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Cum in nesciunt nostrum quae maxime totam. Sint amet officia ipsam enim? Ducimus libero nulla labore nostrum assumenda provident quibusdam fugiat voluptatem.</p>
    
        <label for="">E</label>
        <input type="text">
    </div>
</body>
</html>