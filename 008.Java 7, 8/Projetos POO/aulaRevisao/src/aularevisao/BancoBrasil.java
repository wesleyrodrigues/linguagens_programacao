package aularevisao;

public class BancoBrasil extends Banco {

    @Override
    public float buscarTaxaDeposito() {
        return (float) 0.0;
    }

    @Override
    public float buscarTaxaTransferencia() {
        return (float) 6.5;
    }

    @Override
    public float buscarTaxaSaque() {
        return (float) 1;
    }
    
}
