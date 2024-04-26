<?php
    include('db.php');
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
    <form action="<?php htmlspecialchars($_SERVER['PHP_SELF']); ?>" method="post">
        <p>Clique em "Enviar" para concluir</p>
        <input type="submit" name="back" value="Enviar">
    </form>
</body>
</html>

<?php 
    if(isset($_POST['back'])){
        $pedido_info = [$_SESSION['nome'], $_SESSION['email'], $_SESSION['telefone'], $_SESSION['ativo'], $_SESSION['cpf'], $_SESSION['modalidade'], $_SESSION['curso'], $_SESSION['doc_solicitado']];
        $aluno_info = [$_POST['nome'], $_POST['cpf'], $_POST['telefone'], $_POST['email'], $_POST['ativoAluno']]; 
         
        $inserir_aluno = "INSERT INTO `pedidos`(`nome`, `cpf`, `telefone`, `email`, `ativo` ) VALUES ('$pedido_info[0]','$pedido_info[4]','$pedido_info[2]','$pedido_info[1]','$pedido_info[3]')";
        $conn->query($inserir_aluno);

        $sql = "SELECT id FROM pedidos ORDER BY id DESC LIMIT 1";
        $result = $conn->query($sql);
    
        if ($result && $result->num_rows > 0) {
            $row = $result->fetch_assoc();
            $aluno_id = $row['id'];
        }

        $sql = "SELECT nome, preco FROM tipos_doc WHERE id_tipos_docs = '$pedido_info[7]'";
        $result = $conn->query($sql);

        if ($result && $result->num_rows > 0) {
            $row = $result->fetch_assoc();
            $tipo_documento = $row['nome'];
            $preco_documento = $row['preco'];
        }
                        
        $inserir_pedido = "INSERT INTO `pedidos_docs`(`id_aluno`,`tipo_doc`,`preco_emissao`, `status`) VALUES ('$aluno_id','$tipo_documento','$preco_documento', 1)";
        $conn->query($inserir_pedido);

        // session_destroy();
        header('Location: ../index.php');
    }


    $conn->close();
?>