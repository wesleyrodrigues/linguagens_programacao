package br.ulbra;

import javax.swing.JOptionPane;

public class App {

    public static void main(String[] args) {
        Agenda a = new Agenda();

        while (true) {
            String op = input("Escolha uma opção \n"
                    + "1 - Adicionar um novo contato \n"
                    + "2 - Remover um contato \n"
                    + "3 - Mostrar \n"
                    + "4 - Sair \n"
                    + "Digite: ");

            switch (op) {
                case "1":
                    String nome = input("Digite o nome: ");
                    String telefone = input("Digite o telefone: ");
                    Contato c = new Contato(nome, telefone);
                    a.addContato(c);
                    break;
                case "2":
                    String n = input("Digite o nome do contato que deseja remover: ");
                    Contato contato = null;
                    for (Contato c1 : a.getContatos()) {
                        if (c1.getNome().equals(n)) {
                            contato = c1;
                        }
                    }
                    a.removeContato(contato);
                    break;
                case "3":
                    a.mostrar();
                    break;
                case "4":
                    System.exit(0);
                default:
                    print("Opção inválida.");
            }
        }
    }

    public static void print(String message) {
        System.out.println(message);
    }

    public static String input(String message) {
        return JOptionPane.showInputDialog(message);
    }

}
