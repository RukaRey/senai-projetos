<?php

function createConn($db_server,$db_user,$db_pass,$db_name){
    try{
        echo 'Connected!' . "<br>";
        return mysqli_connect($db_server, $db_user, $db_pass, $db_name);
    }
    catch(mysqli_sql_exception){
        echo 'Could not connect!';
        die;
    }
}

function getData($conexao,$tabela){
    $sql = "SELECT * FROM $tabela";
    
    $saida = [];
    
    $result = mysqli_query($conexao, $sql);
 
    if (mysqli_num_rows($result) > 0) {
        while($row = mysqli_fetch_assoc($result)) $saida[] = $row;
        return $saida;
    }
    else{
        return false;
    }
}

function setData($conn,$tabela){
    $verificar = "SELECT * FROM $tabela";
    return $conn->query($verificar);
}

function setData2($conexao,$tabela, $array){
    $verificar = "SELECT * FROM $tabela";
    $resultado = mysqli_query($conexao, $verificar);
    
    if (mysqli_num_rows($resultado) > 0) {
        if ($tabela == 'cliente'){
            $inserir = "INSERT INTO `$tabela`(`nome`, `email`, `telefone`,`cpf` ) VALUES ('$array[0]','$array[1]','$array[2]','$array[3]')";
            mysqli_query($conexao,$inserir);
        }else if ($tabela == 'avaliacao'){
            $inserir = "INSERT INTO `$tabela`(`id_cliente`, `data_hora`) VALUES ('$array[0]','$array[1]')";
            mysqli_query($conexao,$inserir);
        }

    }
    else{
        return false;
    }
    
}
?>