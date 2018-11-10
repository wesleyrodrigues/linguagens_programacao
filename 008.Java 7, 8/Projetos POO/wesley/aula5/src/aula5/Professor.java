package aula5;

public class Professor extends Pessoa {

	@Override
	public void falar() {
		System.out.println("O professor fala");
	}

	@Override
	public void andar() {
		System.out.println("O professor anda");
	}

}
