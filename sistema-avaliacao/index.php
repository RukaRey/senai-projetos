<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bootstrap demo</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
  <style>
    #linha {
      width: 100%;
      border-bottom: 1px solid #000000;
    }
  </style>
  </head>
  <body>
  <div class="container">
    <h3>Avaliação</h3>

    <div id="linha"></div>

    <p><strong>1 -O serviço foi concluído no prazo?</strong></p>

    <div class="form-check">
        <input class="form-check-input" type="checkbox" name="flexRadioDefault" id="flexRadioDefault1">
        <label class="form-check-label" for="flexRadioDefault1">
            Default checkbox
        </label>
    </div>
    <div class="form-check">
        <input class="form-check-input" type="checkbox" name="flexRadioDefault" id="flexRadioDefault2" checked>
        <label class="form-check-label" for="flexRadioDefault2">
        Default checked checkbox
        </label>
    </div>

    <br>

    <p><strong>1 - Quão satisfeito você está com a qualidade do serviço prestado?</strong></p>
    
    <div class="estrela">
      <a href="javascript:void(0)" onclick="Avaliar(1)">
      <img src="img/star0.png" id="s1"></a> Muito insatisfeito
        
      <br>

      <a href="javascript:void(0)" onclick="Avaliar(2)">
      <img src="img/star0.png" id="s2"></a> Insatisfeito
           
      <br>

      <a href="javascript:void(0)" onclick="Avaliar(3)">
      <img src="img/star0.png" id="s3"></a> Neutro
         
      <br>

      <a href="javascript:void(0)" onclick="Avaliar(4)">
      <img src="img/star0.png" id="s4"></a> Satisfeito
        
      <br>

      <a href="javascript:void(0)" onclick="Avaliar(5)">
      <img src="img/star0.png" id="s5"></a> Muito insatisfeito

      <p id="rating">0 </p>
    </div>

    <div class="texto">
      <div class="mb-3">
        <label for="exampleFormControlTextarea1" class="form-label"><strong>Deixe aqui suas críticas, elogios ou sugestões</strong></label>
        <textarea class="form-control" id="exampleFormControlTextarea1" rows="3"></textarea>
      </div>
    </div>

    <center>
        <button type="button" class="btn btn-primary btn-lg btn-block">Botão</button>
    </center>
    
    <script>
        document.querySelectorAll('.form-check-input').forEach(function(input) {
            input.addEventListener('click', function() {
            document.querySelectorAll('.form-check-input').forEach(function(otherInput) {
                if (otherInput !== input) {
                otherInput.checked = false;
                }
            });
            });
        });
    </script>
    <script src="funcoes.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
</body>
</html>

<?php 
$db_name = "sistema_avaliacao";
$db_server = 'localhost';

include ('php/db.php');
$conn = createConn('localhost','root','','sistema_avaliacao');


print_r (getData($conn,'cliente'));

?>