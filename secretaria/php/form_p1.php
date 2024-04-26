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
    <title>Solicitação de documentos</title>
</head>
<body>
    <div>
        <form action="<?php htmlspecialchars($_SERVER['PHP_SELF']); ?>" method='post'>
            <label for="email">E-mail</label><br>
            <input type="email" name="email" id="email" value="<?php if(isset($_SESSION['email'])) echo $_SESSION['email']; ?>"><br><br>
        
            <label for="nome">Nome completo</label><br>
            <input type="text" name="nome" id="nome" value="<?php if(isset($_SESSION['nome'])) echo $_SESSION['nome']; ?>"><br><br>
            
            <label for="cpf">CPF</label><br>
            <input type="text" name="cpf" id="cpf" value="<?php if(isset($_SESSION['cpf'])) echo $_SESSION['cpf']; ?>"><br><br>

            <label for="telefone">Telefone para contato</label><br>
            <input type="text" name="telefone" id="telefone" value="<?php if(isset($_SESSION['telefone'])) echo $_SESSION['telefone']; ?>"><br><br>

            <label for="">Vínculo com instituição</label><br>

            <input type="radio" id="ativo" name="ativoAluno" value="1" <?php if(isset($_SESSION['ativo']) && $_SESSION['ativo'] == '1') echo "checked"; ?>>
            <label for="ativo">Aluno</label>
            <input type="radio" id="inativo" name="ativoAluno" value="0" <?php if(isset($_SESSION['ativo']) && $_SESSION['ativo'] == '0') echo "checked"; ?>>
            <label for="inativo">Ex-aluno</label><br><br>

            <input type="submit" id='next' name='next' value="Próxima">
        </form>
    </div>
    
</body>
</html>

<?php
    if (isset($_POST['next'])){
        if (!empty($_POST['nome']) && !empty($_POST['email']) && !empty($_POST['cpf']) && !empty($_POST['telefone']) && isset($_POST['ativoAluno'])){
            $_SESSION['nome'] = $_POST['nome'];
            $_SESSION['email'] = $_POST['email'];
            $_SESSION['telefone'] = $_POST['telefone'];
            $_SESSION['ativo'] = $_POST['ativoAluno'];
            $_SESSION['cpf'] = $_POST['cpf'];
            if ($_POST['ativoAluno'] == 1){
                header("Location: form_p2.php"); 
            }else{
                header("Location: form_p3.php"); 
            }
            
        }
    }
    

    $conn->close();
    
?>