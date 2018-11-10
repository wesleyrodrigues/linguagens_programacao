package aula5;

public abstract class Veiculo {
	protected String placa;
	protected String motor;
	protected String chassi;
	protected String mataCachorro;
	
	public abstract void ligar();
	public abstract void acelerar();
}
