package iphone2007;

public class Iphone implements ReprodutorMusical, AparelhoTelefonico, NavegadorInternet{
	
	public Iphone() {
		
	}
	
	/////////////////////////////////////////////////////////
	
	public void tocar() {
		System.out.printf("Musica Tocando\n");
	}
	public void pausar() {
		System.out.println("MUSICA PAUSADA");
	}
	public void selecionarMusica(String musica) {
		System.out.printf("Você selecionou: %s%n", musica);
	}
	//////////////////////////////////////////////////////////
	
	public void ligar(String numero) {
		System.out.printf("Você ligou para: %s%n", numero);
	}
	public void atender() {
		System.out.println("Ligação atendida");
	}
	public void iniciarCorreioVoz() {
		System.out.println("Mensagem do corrio de voz!");
	}
	////////////////////////////////////////////////////////
	
	public void exibirPagina(String url) {
		System.out.printf("Exibindo: %s%n", url);
	}
	public void adicionarNovaAba() {
		System.out.println("Abrindo nova pagina");
	}
	public void atualizarPagina() {
		System.out.println("Pagina atualizada");
	}
	
}
