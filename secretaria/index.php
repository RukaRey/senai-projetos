<?php
    include('php/db.php');
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
    <!-- <?php htmlspecialchars($_SERVER['PHP_SELF']); ?> -->
        <form action="index.php" method='post'>
            <label for="nome">Nome completo</label>
            <input type="text" name="nome" id="nome"><br><br>
            
            <label for="cpf">CPF</label>
            <input type="text" name="cpf" id="cpf"><br><br>

            <label for="email">E-mail</label>
            <input type="email" name="email" id="email"><br><br>

            <label for="telefone">Telefone para contato</label>
            <input type="text" name="telefone" id="telefone"><br><br>

            <label for="">Aluno ativo?</label><br><br>

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
    if (isset($_POST['send'])){
        if (!empty($_POST['nome']) && !empty($_POST['email']) && !empty($_POST['cpf']) && !empty($_POST['telefone']) && !empty($_POST['ativoAluno'])){
            $_SESSION['nome'] = $_POST['nome'];
            $_SESSION['email'] = $_POST['email'];
            $_SESSION['telefone'] = $_POST['telefone'];
            $_SESSION['ativo'] = $_POST['ativoAluno'];
            $_SESSION['cpf'] = $_POST['cpf'];
        
            $cpf_aluno = $_POST['cpf'];
            $nome_aluno = $_POST['nome'];
            $email_aluno = $_POST['email'];
            $ativo_aluno = $_POST['ativoAluno'];
            $cpf_aluno = $_POST['cpf'];

            $sql = "SELECT cpf, nome FROM alunos WHERE cpf = '$cpf_aluno' AND nome = '$nome_aluno'";
            $result = $conn->query($sql);
            
            if ($result->num_rows > 0) {
                echo "Aluno encontrado.";
                header('Location: php/form_emissao.php');
            } 
            // $aluno_info = [$_POST['nome'], $_POST['cpf'], $_POST['telefone'], $_POST['email'], $_POST['ativoAluno']];
        
            // $inserir_aluno = "INSERT INTO `alunos`(`nome`, `cpf`, `telefone`, `email`, `ativo` ) VALUES ('$aluno_info[0]','$aluno_info[1]','$aluno_info[2]','$aluno_info[3]','$aluno_info[4]')";
            // $conn->query($inserir_aluno);
        
                
              
        }
        
    }
    
    
    // Fechar conexão
    $conn->close();
    
?>