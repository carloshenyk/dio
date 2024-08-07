package iphone2007;

public class AppSimulaIphone {

	public static void main(String[] args) {
		Iphone iphone = new Iphone();

		iphone.ligar("81988880000");
		iphone.atender();
		iphone.iniciarCorreioVoz();
		
		iphone.selecionarMusica("Deus Proverea!");
		iphone.tocar();
		iphone.pausar();
		
		iphone.adicionarNovaAba();
		iphone.exibirPagina("dio.me");
		iphone.atualizarPagina();
	}

}
