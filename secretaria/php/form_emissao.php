<?php
    include('../php/db.php');
    $conn = createConn('localhost','root','','db_secretaria');
    $aluno_info = [$_POST['nome'], $_POST['cpf'], $_POST['telefone'], $_POST['email'], $_POST['ativoAluno']];

    $inserir_aluno = "INSERT INTO `alunos`(`nome`, `cpf`, `telefone`, `email`, `ativo` ) VALUES ('$aluno_info[0]','$aluno_info[1]','$aluno_info[2]','$aluno_info[3]','$aluno_info[4]')";
    mysqli_query($conn, $inserir_aluno);

    $aluno_id = "SELECT `id` FROM `alunos` WHERE `cpf` = $aluno_info[1]";
    $result = mysqli_query($conn, $aluno_id);

    while($row = mysqli_fetch_assoc($result)) $saida[] = $row;

    echo "<pre>";

    print_r($saida); #last aluno_ID
?>