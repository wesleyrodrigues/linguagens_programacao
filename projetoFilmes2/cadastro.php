<?php
    include_once "db/filmesDAO.php";
    
    if (($_GET['pagina']=='clientes')&&(!isset($_GET['login']))&&(!isset($_GET['cadastro']))) {
        echo '<table class="table table-striped table-bordered table-hover">';
        echo '  <tr><td><a href="?pagina=clientes&login=login"><h2>Login</h2></a></tr></td>';
        echo '  <tr><td><a href="?pagina=clientes&cadastro=novo"><h2>Cadastre-se</h2></a></tr></td>';
        echo '</table>';
    }
    if (isset($_GET['pagina'])) {
        if (isset($_GET['login'])){
            if ($_GET['login'] == 'login') {
                require_once "login.php";
            }
        }
        if (isset($_GET['cadastro'])){
            if ($_GET['cadastro'] == 'novo') {
                require_once "cadCadastro.php";
            }
        }
    }
    /*
    vetorCliente = ["Willian32","Fachetti23","111312","wilf3achetti@gmail.com2","Rua32 Josefina","31"," ","RO","7.907-452","123456"];
    cadastrarNovoCliente($vetorCliente);
    */
?>
<h4 align="right">
    <a href="javascript:window.history.go(-1)">Voltar</a>
</h4>