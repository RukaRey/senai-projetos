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
            <label for="doc_solicitado">Pedido de emissão de documentos escolares para ex-alunos</label><br>

            <input type="radio" id="seg_via_certi" name="doc_solicitado" value="7">
            <label for="seg_via_certi">2ª via de Certificado - R$ 25,00</label><br>

            <input type="radio" id="seg_via_diploma" name="doc_solicitado" value="8">
            <label for="seg_via_diploma">2ª via de Diploma - R$ 35,00</label><br>

            <input type="radio" id="seg_via_diploma_sup" name="doc_solicitado" value="9">
            <label for="seg_via_diploma_sup">2ª via de Diploma Curso Superior - R$ 120,00</label><br>

            <input type="radio" id="seg_via_hist" name="doc_solicitado" value="10">
            <label for="seg_via_hist">2ª via Historico Escolar - R$ 20,00</label><br>

            <input type="radio" id="decl_concl" name="doc_solicitado" value="11">
            <label for="decl_concl">Declaração de Conclusão - R$ 15,00</label><br>

            <input type="radio" id="decl_aposen" name="doc_solicitado" value="12">
            <label for="decl_aposen">Declaração para Fins de Aposentadoria - R$ 20,00</label><br>

            <input type="radio" id="emen_escolar" name="doc_solicitado" value="6">
            <label for="emen_escolar">Ementa Escolar - R$ 20,00 por disciplina com teto máximo de R$ 100,00</label><br>

            <input type="radio" id="hist_parcial" name="doc_solicitado" value="13">
            <label for="hist_parcial">Histórico Parcial - R$ 15,00</label><br>

            <input type="submit" id='next' name='next' value="Próxima">
            <input type="submit" id='prev' name='prev' value="Anterior">
        </form>
    </div>
    
</body>
</html>

<?php
    if (isset($_POST['next'])){
        if (isset($_POST['doc_solicitado'])){
            $_SESSION['doc_solicitado'] = $_POST['doc_solicitado'];

            header("Location: confirm.php");

        }
        
    }
    if (isset($_POST['prev'])){
        header("Location: form_p1.php"); 
    }


    $conn->close();
    
?>