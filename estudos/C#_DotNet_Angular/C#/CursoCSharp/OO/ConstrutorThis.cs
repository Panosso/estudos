using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CursoCSharp.OO
{
    public class Animal { 
        public string Nome { get; set; }

        public Animal(string nome) {
            Nome = nome;
        }
    }

    public class Cachorro : Animal {
        public double Altura { get; set; }

        public Cachorro(string nome) : base(nome) {
            Console.WriteLine($"Cachorro {nome} inicializado.");
        }

        //Esse contrutor chamara o construtor da classe cachorro que consequentemente chama o construtor da classe Animal
        public Cachorro(string nome, double altura) : this(nome){
            Altura = altura;
        }

        public override string ToString()
        {
            return $"{Nome} tem {Altura}cm de altura";
        }

    }


    class ConstrutorThis
    {
        public static void Executar() {

            var spike = new Cachorro("Spike");

            //Pelos argumentos ele sabe qual construtor pegar
            var max = new Cachorro("Max", 40);

            Console.WriteLine(spike);
            Console.WriteLine(max);

        }

    }
}
