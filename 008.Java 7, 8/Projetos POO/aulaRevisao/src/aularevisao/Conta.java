/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package aularevisao;

/**
 *
 * @author Labin
 */
public class Conta {
    public float saldo;
    public String numero;
    public Cliente cliente;
    public Banco banco;
    
    public void sacar(float valor) {
        System.out.println("Saque de " + valor);
        saldo -= valor;
        saldo -= banco.buscarTaxaSaque();
    }
    
    public void depositar(float valor) {
        System.out.println("Deposito de " + valor);
        saldo += valor;
        saldo -= banco.buscarTaxaDeposito();
    }
    
    public void transferir(Conta destino, float valor) {
         saldo -= valor;
         destino.saldo += valor;
         saldo -= banco.buscarTaxaTransferencia();
   }
    
    public void verSaldo() {
        
    }
    
    public void imprimirExtrato() {
        
    }
}
