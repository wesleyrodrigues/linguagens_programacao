package br.com.aulaestrutura.listas;

public class Aluno {
	
	private String nome;
	
	public void setNome(String nome) {
		this.nome = nome;
	}
	
	public String getNome() {
		return this.nome;
	}
	
	public String toString() {
		return String.format("Aluno: %s", this.nome);
	}
	
	public boolean equals(Object obj) {
		Aluno alunoParaCompararComEste = (Aluno) obj;
		return this.getNome().equals(alunoParaCompararComEste.getNome());
	}

}
