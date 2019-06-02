function alerta(){
    
    alert( "Compra realizada com sucesso" );
}


// TENTATIVA DE CRIAR UM POPUP
function popup(){
    // varWindow = window.open (
    // 'popup.html',
    // 'pagina',
    // "width=350, height=255, top=100, left=110, scrollbars=no " );
    // }
    alert( "Compra realizada com sucesso" );
}



    function criarPopup(){
        newWindow = window.open ('', 'pagina');
        newWindow.document.write ("Este é um novo popup <br/> <img src='imagem.jpg' width='100' height='100'>");
        }