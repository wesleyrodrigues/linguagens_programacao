
public class Banco {

    protected String nome;
    protected String numero;
    protected Conta conta;
    protected double taxa = 1.0;
    protected double taxaSaque = 0.50;
    protected double taxaDeposito = 3.25;
    protected double taxaTransferencia = 0.00;

    public void setNome(String nome) {
        this.nome = nome;
    }

    public void setNumero(String numero) {
        this.numero = numero;
    }

    public void setConta(Conta conta) {
        this.conta = conta;
    }

    public void setTaxa(double taxa) {
        this.taxa = taxa;
    }

    public void setTaxaSaque(double taxaSaque) {
        this.taxaSaque = taxaSaque;
    }

    public void setTaxaDeposito(double taxaDeposito) {
        this.taxaDeposito = taxaDeposito;
    }

    public void setTaxaTranferencia(double taxaTransferencia) {
        this.taxaTransferencia = taxaTransferencia;
    }

    public String getNome() {
        return nome;
    }

    public String getNumero() {
        return numero;
    }

    public Conta getConta() {
        return conta;
    }

    public double getTaxa() {
        return taxa;
    }

    public double getTaxaSaque() {
        return taxaSaque * taxa;
    }

    public double getTaxaDeposito() {
        return taxaDeposito * taxa;
    }

    public double getTaxaTranferencia() {
        return taxaTransferencia * taxa;
    }
}
