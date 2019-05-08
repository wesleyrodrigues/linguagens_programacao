package br.com.aulaestrutura.listas;

public class ListaDuplamenteEncadeada {
	protected NoDuplo cabeca, cauda;
	protected long tamanho;

	public ListaDuplamenteEncadeada() {
		this.cabeca = new NoDuplo(null, null, null);
		this.cauda = new NoDuplo(null, cabeca, null);
		this.tamanho = 0;
		cabeca.setNoProximo(cauda);
	}

	public void adicionaInicio(NoDuplo no) {
		if (tamanho == 0) {
			this.cabeca = no;
			this.cauda = no;
			this.cauda.setNoAnterior(cabeca);
		} else {
			this.cabeca.setNoAnterior(no);
			no.setNoProximo(cabeca);
			this.cabeca = no;
		}
		this.tamanho++;
	}

	public void adicionaFinal(NoDuplo no) {
		if (tamanho == 0) {
			this.cabeca = no;
			this.cauda = no;
			this.cauda.setNoAnterior(cabeca);
		} else {
			no.setNoAnterior(cauda);
			this.cauda.setNoProximo(no);
			this.cauda = no;
		}
		this.tamanho++;
	}

	public void removeNo(String elemento) {
		NoDuplo anterior = null;
		NoDuplo atual = cabeca;

		while (atual.getElemento() != elemento) {
			anterior = atual;
			atual = atual.getNoProximo();
		}

		if (atual.getElemento() == elemento) {
			anterior.setNoProximo(atual.getNoProximo());
			tamanho--;
		} else {
			System.out.println("Elemento não encontrado");
		}
	}

	public long tamanho() {
		return tamanho;
	}

	public boolean estaVazia() {
		return getPrimeiro().getElemento() == null ? true : false; // ternario hehe.
	}

	public NoDuplo getPrimeiro() {
		return cabeca;
	}

	public NoDuplo getUltimo() {
		return cauda;
	}

	public NoDuplo getProximo(NoDuplo no) {
		return no.getNoProximo();
	}

	public String toString() {

		NoDuplo atual = cabeca;
		String parcial = "";

		for (int i = 0; i < tamanho(); i++) {
			parcial += (i + 1) + " ";
			parcial += atual.getElemento();
			parcial += "\n";
			atual = atual.getNoProximo();
		}

		return parcial;
	}

	public String toStringD() { // Retorna lista em forma decrescente.
		NoDuplo atual = cauda;
		String parcial = "";

		for (long i = tamanho(); i > 0; i--) {
			parcial += i + " ";
			parcial += atual.getElemento();
			parcial += "\n";
			atual = atual.getNoAnterior();
		}

		return parcial;
	}
}
