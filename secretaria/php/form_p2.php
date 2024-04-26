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
            <label for="modalidade">Em qual modalidade está matriculado?</label><br>
            <select id="modalidade" name="modalidade">
                <option value="">Escolher</option>
                <option value="aprendizagem_industrial">Aprendizagem Industrial</option>
                <option value="habilitacao_tecnica">Habilitação Técnica</option>
                <option value="iniciacao_profissional">Iniciação Profissional</option>
                <option value="qualificacao_profissional">Qualificação Profissional</option>
            </select> <br><br>

            <label for="curso">Qual curso está matriculado?</label><br>
            <select id="curso" name="curso">
                <option value="">Escolher</option>
                <option value="administracao">Administração</option>
                <option value="almoxarife">Almoxarife</option>
                <option value="automacao_industrial">Automação Industrial</option>
                <option value="auxiliar_de_logistica">Auxiliar de Logística</option>
                <!-- ADICIONAR O RESTO DEPOIS -->
            </select><br><br>
        
            <label for="doc_solicitado">Documento a ser solicitado</label><br>

            <input type="radio" id="decl_trans" name="doc_solicitado" value="1">
            <label for="decl_trans">Declaração de Transferência - R$ 15,00</label><br>

            <input type="radio" id="hist_parcial" name="doc_solicitado" value="1">
            <label for="hist_parcial">Histórico Parcial - R$ 15,00</label><br>

            <input type="radio" id="carta_aprese" name="doc_solicitado" value="1">
            <label for="carta_aprese">Carta de apresentação para estágio optativo - Gratuito</label><br>

            <input type="radio" id="decl_matri" name="doc_solicitado" value="1">
            <label for="decl_matri">Declaração de matrícula - Gratuito</label><br>

            <input type="radio" id="seg_via_carte" name="doc_solicitado" value="1">
            <label for="seg_via_carte">2ª via de carteirinha estudantil - R$ 10,00</label><br>

            <input type="radio" id="emen_escolar" name="doc_solicitado" value="1">
            <label for="emen_escolar">Ementa Escolar - R$ 20,00 por disciplina com teto máximo de R$ 100,00</label><br>

            <input type="radio" id="recuperacao" name="doc_solicitado" value="1">
            <label for="recuperacao">Recuperação - R$ 10,00</label><br><br>
            
            <label for="recuperacao">Observação:</label><br>
            <textarea name="comment" rows="5" cols="40"></textarea><br><br>

            <input type="submit" id='next' name='next' value="Próxima">
            <input type="submit" id='prev' name='prev' value="Anterior">
        </form>
    </div>
    
</body>
</html>

<?php
    if (isset($_POST['next'])){
        if (!empty($_POST['modalidade']) && !empty($_POST['curso']) && !empty($_POST['doc_solicitado'])){
            $_SESSION['modalidade'] = $_POST['modalidade'];
            $_SESSION['curso'] = $_POST['curso'];
            $_SESSION['doc_solicitado'] = $_POST['doc_solicitado'];

            header("Location: confirm.php");

        }
        
    }
    if (isset($_POST['prev'])){
        header("Location: form_p1.php"); 
    }


    $conn->close();
    
?>