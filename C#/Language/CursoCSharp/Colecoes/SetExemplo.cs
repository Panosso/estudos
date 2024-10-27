using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CursoCSharp.Colecoes
{

    class SetExemplo
    {
        public static void Executar() {

            var livro = new Produto("LoT", 50.1);


            // HasSet nao é indexada, portanto qualquer operação com index não pode ser utilizada. E ele não aceita repeticao
            var carinho = new HashSet<Produto>();
            carinho.Add(livro);

            var combo = new HashSet<Produto> {
                new Produto("HP", 100),
                new Produto("Camisa", 50.9),
                new Produto("Short", 10)
            };

            //Adiciona valores ao HashSet
            carinho.UnionWith(combo);
            Console.WriteLine(carinho.Count);
            Console.WriteLine(carinho);
            foreach (var item in carinho) {
                Console.WriteLine(item.Nome);
            }

            Console.WriteLine(carinho.Count);
            carinho.Add(livro);
            Console.WriteLine(carinho.Count);


        }
    }
}
