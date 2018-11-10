package aularevisao;

public class Bradesco extends Banco {

    @Override
    public float buscarTaxaDeposito() {
        return (float) 0.0;
    }

    @Override
    public float buscarTaxaTransferencia() {
        return (float) 9.75;
    }

    @Override
    public float buscarTaxaSaque() {
        return (float) 1.50;
    }
    
}
