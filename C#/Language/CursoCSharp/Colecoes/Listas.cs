using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CursoCSharp.Colecoes
{
    public class Produto {
        public string Nome;
        public double Preco;

        public Produto(string nome, double preco) {
            Nome = nome;
            Preco = preco;
        }

        public override bool Equals(object obj)
        {
            Produto outro = (Produto)obj;

            bool mesmoNome = Nome == outro.Nome;
            bool mesmoPreco = Preco == outro.Preco;

            return base.Equals(obj);
        }

    }



    class Listas
    {
        public static void Executar() {

            var livro = new Produto("LoT", 50.1);


            //Apesar da lista aceitar mais de um tipo de dado, porém quando colocado dentro do <> o tipo do objeto, só aquele tipo de objeto pode ser adicionado.
            var carinho = new List<Produto>();
            carinho.Add(livro);

            var combo = new List<Produto> {
                new Produto("HP", 100),
                new Produto("Camisa", 50.9),
                new Produto("Short", 10)
            };

            carinho.AddRange(combo);
            Console.WriteLine(carinho.Count);
            Console.WriteLine(carinho);
            carinho.RemoveAt(3);
            foreach (var item in carinho) {
                Console.WriteLine(carinho.IndexOf(item));
                Console.WriteLine(item.Nome);
            }

            Console.WriteLine(carinho.Count);
            carinho.Add(livro);
            Console.WriteLine(carinho.Count);


        }
    }
}
