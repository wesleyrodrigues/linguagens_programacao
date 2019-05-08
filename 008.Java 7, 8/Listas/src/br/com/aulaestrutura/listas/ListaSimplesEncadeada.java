package br.com.aulaestrutura.listas;

public class ListaSimplesEncadeada {
	protected NoSimples cabeca, ultimo; // Professor deixou colocar ultimo
	protected long tamanho = 0;

	public void adicionaElementoInicio(NoSimples novoElemento) {
		if (tamanho == 0) {
			this.cabeca = novoElemento;
			this.ultimo = novoElemento;
		} else {
			novoElemento.setProximoNo(cabeca);
			this.cabeca = novoElemento;
		}
		this.tamanho++;
	}

	public void adicionaElementoFinal(NoSimples novoElemento) {
		if (tamanho == 0) {
			this.cabeca = novoElemento;
			this.ultimo = novoElemento;
		} else {
			this.ultimo.setProximoNo(novoElemento);
			this.ultimo = novoElemento;
		}

		this.tamanho++;
	}
// não deu tempo de fazer
//	public void removeElemento(String nomeElemento) {
//		NoSimples elemAnt = cabeca;
//		NoSimples elemAtual = cabeca.getProximoNo();
//		NoSimples elemNull;
//		
//		if(tamanho == 0 && cabeca.getElemento() == nomeElemento) {
//			
//			this.cab
//			this.tamanho--;
//		} else {
//			for(int i = 0; i < tamanho; i++) {
//				
//			}
//		}
//		
//	}
	

	public void mostraElementos() {
		NoSimples percoElementos = cabeca; // percorre elementos
		while (percoElementos.getProximoNo() != null) {
			System.out.println(percoElementos.getElemento());
			percoElementos = percoElementos.getProximoNo();
		}
		System.out.println(percoElementos.getElemento());
	}

	public boolean listaContemElemento(String nomeElemento) {
		NoSimples elemento = cabeca;
		for (int i = 0; i < tamanho; i++) {
			if (elemento.getElemento() == nomeElemento) {
				return true;
			}
			elemento = elemento.getProximoNo();
		}
		return false;
	}

	public long getTamanho() {
		return tamanho;
	}
}
