using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CursoCSharp.ClassesEMetodos
{

    public class Produto {
        public string Nome;
        public double Preco;

        /*Quando colocado o termo static, fazendo com que esse atributo deixe de ser de instancia e passe a ser da classe,
         * sendo assim, todos os objetos teram o mesmo valor desse atributo.
         * E ele não pode ser definido pelo objeto, apenas pela classe.
         */
        public static double Desconto;

        public Produto(string nome, double preco, double desconto) {
            Nome = nome;
            Preco = preco;
            Desconto = desconto;
        }

        public Produto() { 

        }

        public double PrecoComDesconto() {
            return Preco - Preco * Desconto / 100;
        }

        public string DescricaoProdu() {
            return $"Produto: {Nome} tem o preço R${Preco} e está com {Desconto}% de desconto";
        }

    }

    class AtributoEstático
    {
        public static void Executar() {
            var prod1 = new Produto("Caneta", 100, 10);
            var prod2 = new Produto()
            {
                Nome = "Borracha",
                Preco = 10
            };

            Produto.Desconto = 50;

            Console.WriteLine(prod1.PrecoComDesconto());
            Console.WriteLine(prod2.PrecoComDesconto());

            Console.WriteLine(prod1.DescricaoProdu());
            Console.WriteLine(prod2.DescricaoProdu());


        }
    }
}
