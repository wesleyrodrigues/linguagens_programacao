package aula5;

public class Run2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Veiculo s10Aleff = new S10();
		Veiculo hornetFabricio = new Titan150();
		
		Moto moto1 = new Titan150();
		Carro carro2 = new S10();
	}

	public void vender(Veiculo v) {
		v.ligar();
		v.acelerar();
		System.out.println(v.placa);
	}
}
