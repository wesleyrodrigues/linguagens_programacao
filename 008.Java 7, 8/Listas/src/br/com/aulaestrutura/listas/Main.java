package br.com.aulaestrutura.listas;

public class Main {

	public static void main(String[] args) {

//		Aluno alunoA = new Aluno();		
//		alunoA.setNome("Willian");
//		
//		Aluno alunoB = new Aluno();		
//		alunoB.setNome("Yard");
//		
//		ListaAlunos lista = new ListaAlunos();
//		lista.adicionaAluno(alunoA);
//		lista.adicionaAluno(alunoB);
//		
//		System.out.println("Lista atual de alunos:");
//		for(int i = 0; i < lista.getTamanho(); i++) {
//			System.out.println(lista.pegaAluno(i).getNome());
//		}
//		
		
		
//		if(lista.listaContemAluno("Yard")) {
//			System.out.println("O aluno está na lista");
//		}
//		
//		System.out.println("");
//		System.out.println("Lista com exclusão");
//		lista.removeNaPosicao(1);
//		for(int i = 0; i < lista.getTamanho(); i++) {
//			System.out.println(lista.pegaAluno(i).getNome());
//		}
//		
//		lista.adicionaAluno(alunoB);
//		
//		System.out.println("");
//		System.out.println("Lista com adição");
//		for(int i = 0; i < lista.getTamanho(); i++) {
//			System.out.println(lista.pegaAluno(i).getNome());
//		}
//		
//		Aluno alunoC = new Aluno();
//		alunoC.setNome("Tata");
//				
//		System.out.println("");
//		System.out.println("Lista com item adicionado em posição");
//		lista.adicionaNaPosicao(1,alunoC);
//		for(int i = 0; i < lista.getTamanho(); i++) {
//			System.out.println(lista.pegaAluno(i).getNome());
//		}
//		String aluno[] = new String[100];
//		int vetor[] = { 0, 5, 7, 2, 1, 3, 6, 9, 8, 4 };
		// ordFuncaoSimples(vetor);
//        ordFuncaoRecursiva(vetor);

//		for (int i = 0; i < 10; i++) {
//			System.out.println(vetor[i]);
//		}
		ListaSimplesEncadeada lista1 = new ListaSimplesEncadeada();
		NoSimples no = new NoSimples();
		NoSimples no1 = new NoSimples();
		NoSimples no2 = new NoSimples();
		NoSimples no3 = new NoSimples();
		
		no1.setElemento("Wesley");
		no2.setElemento("Wellyngton");
		no3.setElemento("Pedro");
		
		no.setElemento("willian");
		
		lista1.adicionaElementoInicio(no1);
		lista1.adicionaElementoInicio(no2);
		lista1.adicionaElementoInicio(no3);
		lista1.adicionaElementoFinal(no);
//		lista1.mostraElementos();
		
//		System.out.println(lista1.listaContemElemento("willian"));
		
		NoDuplo noD = new NoDuplo("um", null, null);
		NoDuplo noD1 = new NoDuplo("dois", null, null);
		NoDuplo noD2 = new NoDuplo("tr�s", null, null);
		NoDuplo noD3 = new NoDuplo("primeiro", null, null);
		NoDuplo noD4 = new NoDuplo("Antes do primeiro", null, null);
		
		ListaDuplamenteEncadeada listaD = new ListaDuplamenteEncadeada();
		System.out.println(listaD.estaVazia());
		listaD.adicionaFinal(noD);
		System.out.println(listaD.estaVazia());
		listaD.adicionaFinal(noD1);
		listaD.adicionaFinal(noD2);
		listaD.adicionaInicio(noD3);
		listaD.adicionaInicio(noD4);
		listaD.removeNo("tr�s");
		System.out.println(listaD.toString());
	}

    public static void ordFuncaoRecursiva(int [] vetor){
        boolean bool = false;
        for(int i = 0; i < 9; i++){
                if (vetor[i] > vetor[i + 1]) {
                    bool = true;
                    int a = vetor[i];
                    vetor[i] = vetor[i + 1];
                    vetor[i + 1] = a;
                }
            }
        if(bool){
            ordFuncaoRecursiva(vetor);
        }
    }

	public static void ordFuncaoSimples(int[] vetor) {
		boolean bool = true;
		while (bool) {
            bool = false;
            for(int i = 0; i < 9; i++){
                if (vetor[i] > vetor[i + 1]) {
                    bool = true;
                    int a = vetor[i];
                    vetor[i] = vetor[i + 1];
                    vetor[i + 1] = a;
                }
            }
		}
	}

}