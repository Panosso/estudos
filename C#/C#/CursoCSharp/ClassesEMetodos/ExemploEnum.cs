using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CursoCSharp.ClassesEMetodos
{


    public enum Genero { Acao, Aventura, Terror, Animacao};

    public class Filme {
        public string Titulo;
        public Genero GeneroFilme;
    }

    class ExemploEnum
    {

        public static void Executar() {

            //Converte o index do item como inteiro, nesse exemplo será o 3
            int id = (int)Genero.Animacao;
            Console.WriteLine(id);

            var FilmeFamilia = new Filme();
            FilmeFamilia.Titulo = "Sharknado";
            FilmeFamilia.GeneroFilme = Genero.Aventura;

            Console.WriteLine(FilmeFamilia.Titulo);
            Console.WriteLine(FilmeFamilia.GeneroFilme);

        }

    }
}
