<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>SL Filmes</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" type="text/css" media="screen" href="css/estilos.css">
    <script src="js/main.js"></script>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
        integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
</head>
<style>
       a:link,
    a:visited {
        color: red;
        text-decoration: none;
    }

    a:hover {
        color: aliceblue;
    }


    a.nounderline:link /*CLASSE PARA TIRAR O SUBLINHADO DO LINK*/
    { 
    text-decoration:none; 
    
    } 
    </style>
    
<body background="img/vingadores.png">
    <!--AQUI É A BARRA DE NAVEGAÇÃO -->
    <div class='row'>
        <div class='col-sm-12'>
            <nav class="navbar  navbar-expand-lg navbar-dark bg-ligth" style="background-color:black">
                    
                    <a class="navbar-brand" href="index.php">SL Filmes</a>
                    <button class="navbar-toggler" aria-expanded="false" aria-controls="navbarSupportedContent" aria-label="Toggle navigation" type="button" data-target="#navbarSupportedContent" data-toggle="collapse">
                        <span class="navbar-toggler-icon"></span> </button>
                            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                                <ul class="navbar-nav mr-auto">
                                    <li class="nav-item ">
                                        <a class="nav-link" href="index.php">INICIO</a>
                                    </li>
                                    <li class="nav-item">
                                        <a class="nav-link" href="cadastro.php">COMPRA DE INGRESSOS</a>
                                    </li>
                                    <li class="nav-item">
                                        <!-- NÃO ESTA FUNCIONANDO, ESTA INDO EM EXIBIÇAO.HTML -->
                                        <a class="nav-link " href="exibicao.php">EXIBIÇÃO</a>
                                    </li>
                                </ul>  
                            </div>
                </nav>
        </div>
    </div>
                           
            <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>
            <script src="js/bootstrap.min.js"></script>

    
</body>

</html>