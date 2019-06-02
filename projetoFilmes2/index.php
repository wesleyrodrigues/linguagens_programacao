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
<body>
            <!-- codigo do professor -->
        <div class='row'>
            <div class='col-sm-12'>

                <?php include("cabecalho.php") ?>

            </div>  
        </div>
        <div class='container-fluid'>
            <div role="main">
                <div class="row">
                        
                        <div class='col-sm-1 center2 hover-image span'></div>
                        <!--IMAGEM 01 CAPITÃ MARVEL-->
                        <div class=" col-sm-2 center2 hover-image span" id="fonte1">
                            <a href="exibicao.php"><img width="140" height="190" class='imgA' src="img/capita.jpg"></a>
                            <span class="texto fonte1">EM EXIBIÇÃO</span>
                            <br><a  class='nounderline fontDescricao' href="exibicao.php" > CAPITÃ MARVEL </a>
                            
                        </div>
                        <!--IMAGEM 02 DUMBO-->
                        <div class=" col-sm-2 center2 hover-image span" id="fonte1">
                            <a href="exibicao.php"><img width="140" height="190" class="imgA" src="img/dumbo.jpg"></a>
                            <span class="texto fonte1">EM EXIBIÇÃO</span>
                            <br><a class='nounderline' href="exibicao.php"> DUMBO </a>
                        </div>
                            <!--IMAGEM 03 SHAZAM-->
                        <div class=" col-sm-2 center2 hover-image span" id="fonte1">
                            <a href="exibicao.php"><img width="140" height="190" class="imgA" src="img/shazam.jpg"></a>
                            <span href = "exibicao.php" class="texto fonte1">EM EXIBIÇÃO</span>
                            <br><a class='nounderline' href="exibicao.php"> SHAZAM! </a>
                        </div>
                        <!--IMAGEM 04 VINGADORES-->
                        <div class=" col-sm-2 center2 hover-image span" id="fonte1">
                                <a href="#"><img width="140" height="190" class="imgA" src="img/vingadores1.jpg"></a>
                                <!-- CRIAR UMA PAG DE EM BREVE -->
                                <span class="texto fonte1">EM BREVE</span>
                                <br><a class='nounderline' href="#"> VINGADORES </a>
                            </div>
                        <div class='col-sm-1 center2 hover-image span'></div>

                </div>
            </div>
    
        <?php
        if (!isset($_GET['pagina'])) {
            echo '<table class="table table-striped table-bordered table-hover">';
            echo '  <tr><td><a href="?pagina=administrar"><h2>Administração</h2></a></tr></td>';
            echo '  <tr><td><a href="?pagina="><h2>Produtos</h2></a></tr></td>';
            echo '  <tr><td><a href="?pagina=clientes"><h2>Clientes</a></h2></tr></td>';
            echo '</table>';
        }
        if (isset($_GET['pagina'])) {
            if ($_GET['pagina'] == 'produtos') {
                require_once "indexProduto.php";
            }
            if ($_GET['pagina'] == 'clientes') {
                require_once "indexClientes.php";
            }
            if ($_GET['pagina'] == 'administrar') {
                require_once "indexAdministrar.php";
            }
        }
        ?>
        <footer class="footer">
            <p align="center">Todos Direitos reservados SL Filmes.</p>
        </footer>
    </div>
</body>



<!-- O que está acontecendo aqui essa budega não funfun -->
<!-- <style>
       a:link,
    a:visited {
        color: blue;
        text-decoration: none;
    }

    a:hover {
        color: aliceblue;
    }


    a.nounderline:link /*CLASSE PARA TIRAR O SUBLINHADO DO LINK*/
    { 
    text-decoration:none; 
   
    
    } 
    </style> -->
    

<body>
    <!-- Donde você tirou isso -->
    <!-- <div class="img-responsive" background="img/vingadores.png"> -->
    
    </div>
    <!--AQUI É A BARRA DE NAVEGAÇÃO INCLUIDA POR PHP -->
    <div class='row'>
        <div class='col-sm-12'>

            <?php include("cabecalho.php") ?>

        </div>
    </div>
            <!--CONTEUDO AO MEIO FILMES ETC-->        
    </header>
        <div class='container-fluid'>
            <div role="main">
                <div class="row">
                        <!--MEXE NÃO, TA FUNCIONANDO E TA ESTRUTURADO, É MUDAR UMA VIRGURA DA MERDA NISSO KKKKKKKK-->
                        
                        <div class='col-sm-1 center2 hover-image span'></div>
                        <!--IMAGEM 01 CAPITÃ MARVEL-->
                        <div class=" col-sm-2 center2 hover-image span" id="fonte1">
                            <a href="exibicao.php"><img width="140" height="190" class='imgA' src="img/capita.jpg"></a>
                            <span class="texto fonte1">EM EXIBIÇÃO</span>
                            <br><a  class='nounderline fontDescricao' href="exibicao.php" > CAPITÃ MARVEL </a>
                            
                        </div>
                        <!--IMAGEM 02 DUMBO-->
                        <div class=" col-sm-2 center2 hover-image span" id="fonte1">
                            <a href="exibicao.php"><img width="140" height="190" class="imgA" src="img/dumbo.jpg"></a>
                            <span class="texto fonte1">EM EXIBIÇÃO</span>
                            <br><a class='nounderline' href="exibicao.php"> DUMBO </a>
                        </div>
                            <!--IMAGEM 03 SHAZAM-->
                        <div class=" col-sm-2 center2 hover-image span" id="fonte1">
                            <a href="exibicao.php"><img width="140" height="190" class="imgA" src="img/shazam.jpg"></a>
                            <span href = "exibicao.php" class="texto fonte1">EM EXIBIÇÃO</span>
                            <br><a class='nounderline' href="exibicao.php"> SHAZAM! </a>
                        </div>
                        <!--IMAGEM 04 VINGADORES-->
                        <div class=" col-sm-2 center2 hover-image span" id="fonte1">
                                <a href="#"><img width="140" height="190" class="imgA" src="img/vingadores1.jpg"></a>
                                <!-- CRIAR UMA PAG DE EM BREVE -->
                                <span class="texto fonte1">EM BREVE</span>
                                <br><a class='nounderline' href="#"> VINGADORES </a>
                            </div>
                        <div class='col-sm-1 center2 hover-image span'></div>

                </div>
            </div>


            <!--BOTÃO DE COMPRE AGORA SEU INGRESSO-->
            
            <div class='container-fluid'>
                    <div role="main">
                        <div class="row">
                            <div class="col-sm-4" ></div>

                            <div class="col-sm-4"id="btnCompreIngresso">
                                <a href="cadastro.php"><button  type="button"  class="btn btn-danger btn-lg">CLIQUE PARA COMPRAR SEU INGRESSO</button></a>
                            </div>

                            <div class="col-sm-4"></div>
                           
                            </div>
                     </div>
             </div>
        
        </div>
        


     
        <!--RODAPÉ DP SITE-->
                <footer>
                    <div class="container-fluid">
                        <div class='row'>
                                <div class="row">
                                        <div class='col-sm-12'style="color: #FFF; top: 50px; left: 135%;"> TODOS OS DIREITOS RESERVADOS © SL FILMES </div>
                </footer>
             </div> 
                    
            <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>
            <script src="js/bootstrap.min.js"></script>

    
</body>

</html>