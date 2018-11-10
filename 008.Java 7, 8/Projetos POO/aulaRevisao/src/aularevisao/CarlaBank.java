package aularevisao;


public class CarlaBank extends Banco {

    @Override
    public float buscarTaxaDeposito() {
        return (float) 0.0;
    }

    @Override
    public float buscarTaxaTransferencia() {
        return (float) 3.25;
    }

    @Override
    public float buscarTaxaSaque() {
        return (float) 0.50;
    }
    
}
