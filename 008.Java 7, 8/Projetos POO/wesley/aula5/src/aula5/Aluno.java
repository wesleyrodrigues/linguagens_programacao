package aula5;

public class Aluno extends Pessoa{

	@Override
	public void falar() {
		System.out.println("O aluno fala");
	}

	@Override
	public void andar() {
		System.out.println("O aluno anda");
	}


}
