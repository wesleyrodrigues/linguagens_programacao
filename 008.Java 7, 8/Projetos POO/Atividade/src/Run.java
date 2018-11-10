
public class Run {

    public static Conta criarConta(String nomeCliente, String cpf, String nomeBanco, String numeroBanco, String numeroConta, double saldo, double taxa) {

        Cliente cliente = new Cliente();
        Banco banco = new Banco();
        Conta conta = new Conta();

        cliente.setNome(nomeCliente);
        cliente.setCpf(cpf);

        banco.setConta(conta);
        banco.setNome(nomeBanco);
        banco.setNumero(numeroBanco);
        banco.setTaxa(taxa);

        conta.setBanco(banco);
        conta.setConta(numeroConta);
        conta.setCorrentista(cliente);
        conta.setSaldo(saldo);
        conta.setExtrato("      Extrato\n"
                + nomeBanco + "\nConta: "
                + numeroConta + "    Banco: "
                + numeroBanco + "\n");
        return conta;
    }

    public static void main(String args[]) {
        Conta cliente1 = criarConta("Kiko", "041.897.554-77", "Carla Bank", "002", "00001", 1000.00, 1.0);
        Conta cliente2 = criarConta("Chaves", "044.888.778-47", "Carla Bank", "002", "00002", 0.00, 1.0);
        Conta cliente3 = criarConta("Sr. Madruga", "478.444.897-58", "Bradesco", "003", "00001", 20.00, 3.0);
        Conta cliente4 = criarConta("Prof. Girafales", "467.897.547-71", "Banco do Brasil", "004", "00001", 500.00, 2 / 3.0);

        cliente1.tranferir(cliente2, 100.00);
        cliente4.tranferir(cliente3, 180.00);

        cliente1.depositar(500.00);
        cliente2.depositar(10.00);
        cliente3.depositar(20.00);
        cliente4.depositar(50.00);

        cliente1.sacar(150.00);
        cliente2.sacar(15.00);
        cliente3.sacar(50.00);
        cliente4.sacar(20.00);

        Conta clientes[] = {cliente1, cliente2, cliente3, cliente4};

        for (Integer i = 0; i < 4; i++) {
            clientes[i].imprimeExtrato();
        }

        for (Integer i = 0; i < 4; i++) {
            clientes[i].impressao();
        }
    }
}
