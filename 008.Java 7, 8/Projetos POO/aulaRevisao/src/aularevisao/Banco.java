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
public abstract class Banco {
    public String nome;
    public String numero;
    
    public abstract float buscarTaxaDeposito();
    public abstract float buscarTaxaTransferencia();
    public abstract float buscarTaxaSaque();
//    public buscarTaxa();
}
