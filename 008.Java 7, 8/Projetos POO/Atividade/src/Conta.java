
import java.util.Calendar;
import java.util.Date;

public class Conta {

    protected String conta;
    protected Banco banco;
    protected Cliente correntista;
    protected double saldo;
    protected String extrato;

    public void setConta(String conta) {
        this.conta = conta;
    }

    public void setBanco(Banco banco) {
        this.banco = banco;
    }

    public void setCorrentista(Cliente correntista) {
        this.correntista = correntista;
    }

    public void setSaldo(double saldo) {
        this.saldo = saldo;
    }

    public void setExtrato(String extrato) {
        this.extrato = extrato;
    }

    public String getConta() {
        return conta;
    }

    public Banco getBanco() {
        return banco;
    }

    public Cliente getCorrentista() {
        return correntista;
    }

    public double getSaldo() {
        return saldo;
    }

    public String getExtrato() {
        return extrato;
    }

    public void tranferir(Conta contaDestino, double valor) {
        if (valor <= saldo) {
            double saldoDestino = contaDestino.getSaldo();
            this.saldo = saldo - valor - banco.getTaxaTranferencia();
            contaDestino.saldo = saldoDestino + valor;
            System.out.println("Transferência efetuada");

            Date hora = Calendar.getInstance().getTime();
            String novoExtrato = "Valor transferido "
                    + valor + " da conta " + conta
                    + " do banco: " + banco.getNome()
                    + " para a conta " + contaDestino.getConta()
                    + " do banco: " + contaDestino.getBanco().getNome() + "\nHora: "
                    + hora + "\n";
            this.extrato = this.extrato + novoExtrato;
            contaDestino.setExtrato(contaDestino.getExtrato() + novoExtrato);
        } else {
            System.out.println("Valor de saldo insuficiente");
        }
    }

    public void sacar(double valor) {
        if (valor <= saldo) {
            this.saldo = saldo - valor - banco.getTaxaSaque();
            System.out.println("Saque efetuado");
            Date hora = Calendar.getInstance().getTime();
            String novoExtrato = "Valor sacado "
                    + valor + " da conta " + conta
                    + " do banco: " + banco.getNome()
                    + "\nHora: " + hora + "\n";

            this.extrato = this.extrato + novoExtrato;
        } else {
            System.out.println("Valor insuficiente");
        }
    }

    public void depositar(double valor) {
        if (valor >= 0) {
            this.saldo = saldo + valor - banco.getTaxaDeposito();
            Date hora = Calendar.getInstance().getTime();
            String novoExtrato = "Valor depositado "
                    + valor + " na conta " + conta
                    + " do banco: " + banco.getNome()
                    + "\nHora: " + hora + "\n";
            this.extrato = this.extrato + novoExtrato;
            System.out.println("Deposito feito com sucesso");
        } else {
            System.out.println("Valor insuficiente\nDigite valor maior que 0.00");
        }

    }

    public void imprimeExtrato() {
        System.out.println(extrato);
    }

    public void impressao() {
        System.out.println("       " + banco.getNome());
        System.out.println("Conta: " + conta + "    Banco: " + banco.getNumero());
        System.out.println("Correntista: " + correntista.getNome());
        System.out.printf("Saldo atual: R$ %.2f\n\n", (saldo));
    }
}
