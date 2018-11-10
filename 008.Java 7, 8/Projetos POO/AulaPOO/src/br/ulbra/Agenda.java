package br.ulbra;

import java.util.ArrayList;

public class Agenda {
    private ArrayList<Contato> contatos = new ArrayList<>();
    
    public void addContato(Contato contato){
        this.contatos.add(contato);
    }

    public ArrayList<Contato> getContatos() {
        return contatos;
    }
    
    public void removeContato(Contato contato){
        this.contatos.remove(contato);
    }
    public void mostrar() {
        for(Contato c: this.contatos){
            System.out.println(c);
        }
    }
}
