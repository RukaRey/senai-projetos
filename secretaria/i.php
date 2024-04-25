<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
  <title>Senai</title>
  <style>
    body, html {
      height: 100%;
      margin: 0; /* Remover margens padrão */
      padding: 0; /* Remover preenchimento padrão */
    }

    .container {
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      height: 100%;
    }

    .container2 {
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      margin-top: 20px; /* Adicionado um pequeno espaço */
      margin-bottom: 10px; /* Espaço entre o formulário e o rodapé */
    }

    .azul {
      background-color: #005caa !important;
      color: white;
      border: 1px solid ;
      width: 100%; 
    }

    .navbar-brand {
      display: flex;
      align-items: center;
    }

    .navbar-brand img {
      margin-right: 10px; 
    }

    footer {
      background-color: #005caa ;
      color: white;
      padding: 20px;
      text-align: center;
      width: 100%;
      position: fixed; /* Manteve o rodapé fixo */
      bottom: 0;
    }

    .p1 {
        color: white;
        font-size: 24px;
    }

    .p2 {
      font-size: 20px;
      margin-top: 0; 
      margin-bottom: -5px; 
    } 
    

    .h1 {
        color: gray;
        font-size: 60px;
        margin-top: 0; 
    }

    h1, p {
      text-align: center; 
    }

    .custom-form {
      background-color:  #005caa; /* Cor de fundo do formulário */
      padding: 20px;
      border-radius: 10px;
      color: white; /* Cor do texto dentro do formulário */
    }

    .custom-form input[type="email"] {
      color: white; /* Cor do texto dentro dos campos de entrada */
    }

    .custom-form label {
      color: white; /* Cor do texto dos rótulos */
    }

    .custom-form button[type="submit"] {
      margin-top: 10px; /* Adicionado espaço acima do botão */
      background-color: #005caa; /* Cor de fundo do botão */
      border-color: white; /* Cor da borda do botão */
    }

    input {
        border: 1px solid white; /* Define a borda com cor branca */
        padding: 5px; /* Apenas para dar um espaçamento interno ao input */
    }
  </style>
</head>
<body>
  <nav class="navbar navbar-light bg-light azul">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">
        <img src="https://logodownload.org/wp-content/uploads/2019/08/senai-logo-7.png" alt="" width="300" height="70" class="d-inline-block align-text-top">
        <p class="p1">SENAI Mergulhão</p>
      </a>
    </div>
  </nav>
  <h1 class="h1">Solicitação de documentos</h1>
  <!-- noooooossa -->
    <div class="container2">
      <form action="php/form_emissao.php" method='post' class="custom-form"> <!-- Adicionei a classe custom-form aqui -->
          <label for="exampleInputEmail1" class="form-label">Nome completo</label>
          <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
         
          <label for="exampleInputEmail1" class="form-label">CPF</label>
          <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">


          <label for="exampleInputEmail1" class="form-label">E-mail</label>
          <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">


          <label for="exampleInputEmail1" class="form-label">Telefone</label>
          <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">

          <label for="">Ativo?</label><br><br>

          <div class="form-check">
          <input class="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault1">
          <label class="form-check-label" for="flexRadioDefault1">
            Sim
          </label>
        </div>
        <div class="form-check">
          <input class="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault2" checked>
          <label class="form-check-label" for="flexRadioDefault2">
            Não
          </label>
          </div>

          <button type="submit" class="btn btn-primary azul">Enviar</button>
      </div>
    </form>
  </div>
  </div>
  <footer>
    SENAI JUIZ DE FORA CFP JOSÉ FAGUNDES NETTO<br>
    03.773.700/0017-74<br>
    Avenida Barão do Rio Branco, 1219 - Centro - Juiz de Fora - CEP: 36035-000<br>
    Telefone: 32 3239-2233
  </footer>
</body>
</html>