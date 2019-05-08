package br.com.aulaestrutura.listas;

public class ListaAlunos {
	
	private Aluno listaAlunos[] = new Aluno[100];
	private int tamanhoLista = 0;
	
	//1) Adiciona um dado no fim da Lista.		
	public void adicionaAluno(Aluno novoAluno) {		
		this.listaAlunos[this.tamanhoLista] = novoAluno;	
		this.tamanhoLista++;
	}
	
	//2) Adiciona um dado em uma dada posição.
	public void adicionaNaPosicao(int posicao, Aluno aluno) {		
		for(int i = this.getTamanho() - 1 ; i >= posicao; i--) {
			this.listaAlunos[i+1] = this.listaAlunos[i];
		}
		this.listaAlunos[posicao]= aluno;
		this.tamanhoLista++;		
	}
	
	//3) Pega o dado de determinada posição.	
	public Aluno pegaAluno(int posicao) {
		return this.listaAlunos[posicao];
	}
	
	//4) Remove o dado de determinada posição.
	public void removeNaPosicao(int posicao) {
		for (int i = posicao; i < this.getTamanho(); i++) { 
			this.listaAlunos[i] = this.listaAlunos[i + 1];	
		}
		this.tamanhoLista--;
	}
	
	//5) Verifica se um dado está armazenado.
	public boolean listaContemAluno(String nomeAluno) {
		for(int i = 0; i < this.getTamanho(); i++) {
			if(listaAlunos[i].getNome().equals(nomeAluno)) {
				return true;
			}
		}
		return false;
	}
	
	//6) Informa o número de registros armazenados.
	public int getTamanho() {
		return this.tamanhoLista;
	}
	
	
}
