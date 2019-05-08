package br.com.aulaestrutura.listas;

public class NoSimples {
	String elemento;
	NoSimples proximoNo;
	
	public String getElemento() {
		return elemento;
	}
	public void setElemento(String elemento) {
		this.elemento = elemento;
	}
	
	public NoSimples getProximoNo() {
		return proximoNo;
	}
	
	public void setProximoNo(NoSimples proximoNo) {
		this.proximoNo = proximoNo;
	}
}
