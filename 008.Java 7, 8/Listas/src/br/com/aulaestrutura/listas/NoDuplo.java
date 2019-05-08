package br.com.aulaestrutura.listas;

public class NoDuplo {
	private String elemento;
	private NoDuplo noAnterior;
	private NoDuplo noProximo;

	public NoDuplo(String e, NoDuplo noA, NoDuplo noP) {
		this.elemento = e;
		this.noAnterior = noA;
		this.noProximo = noP;
	}

	public void setElemento(String elemento) {
		this.elemento = elemento;
	}

	public void setNoAnterior(NoDuplo noAnterior) {
		this.noAnterior = noAnterior;
	}

	public void setNoProximo(NoDuplo noProximo) {
		this.noProximo = noProximo;
	}

	public String getElemento() {
		return elemento;
	}

	public NoDuplo getNoAnterior() {
		return noAnterior;
	}

	public NoDuplo getNoProximo() {
		return noProximo;
	}
}
