<?php
    include('php/db.php');
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
    <!-- <?php htmlspecialchars($_SERVER['PHP_SELF']); ?> -->
        <form action="index.php" method='post'>
            <label for="nome">Nome</label>
            <input type="text" name="nome" id="nome"><br><br>
            
            <label for="cpf">CPF</label>
            <input type="text" name="cpf" id="cpf"><br><br>

            <label for="email">E-mail</label>
            <input type="email" name="email" id="email"><br><br>

            <label for="telefone">Telefone</label>
            <input type="text" name="telefone" id="telefone"><br><br>

            <label for="">Ativo?</label><br><br>

            <input type="radio" id="ativo" name="ativoAluno" value="1">
            <label for="ativo">Sim</label>
            <input type="radio" id="inativo" name="ativoAluno" value="0">
            <label for="inativo">Não</label><br>

            <input type="submit" id='send' name='send'>
        </form>
    </div>
    
</body>
</html>

<?php
    
?>