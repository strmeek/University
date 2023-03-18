public class Main {
    public static void main(String[] args) {
        //Cria locadora
        Locadora locadora = new Locadora();

        //cria discos na memória
        Disco disco1 = new Disco("Samba Social Clube 5", 2014, "Vários Sambas", "Vários Artistas", 12, "CD");
        Disco disco2 = new Disco("Pode Entrar", 2009, "Ivete e Convidados", "Ivete Sangalo", 14, "DVD");

        //cria filmes na memória
        Filme filme1 = new Filme("Smurfs 2", 2013, "Gargamel cria a versão malvada dos Smurfs", "Raja Gosnell", 140, "Animação");
        Filme filme2 = new Filme("Os mercenários 2", 2012, "De volta ao mundo", "Simon West", 210, "Animação");

        //adiciona tudo aos arrays da locadora
        locadora.novoDisco(disco1);
        locadora.novoDisco(disco2);
        locadora.novoFilme(filme1);
        locadora.novoFilme(filme2);

        //Resultado
        System.out.println("-----------------Discos------------------");
        System.out.println("-----------------------------------------");
        locadora.ListarDiscos();

        System.out.println("-----------------Filmes------------------");
        System.out.println("-----------------------------------------");
        locadora.ListarFilmes();
    }
}