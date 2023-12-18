using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CursoCSharp.ClassesEMetodos
{

    public class Dependente {
        public string Nome;
        public int Idade;
    }

    class ValorVSReferencia
    {
        public static void Executar() {
            int numero =  3;
            int numeroCopia = 3;
            numero++;

            //Por valor
            Console.WriteLine(numero);
            Console.WriteLine(numeroCopia);

            Dependente dep = new Dependente
            {
                Nome = "Pedro",
                Idade = 20
            };

            // Por referencia, de memoria.
            Dependente copiaDep = dep;

            Console.WriteLine($"{dep.Nome}, {copiaDep.Nome}");
            Console.WriteLine($"{dep.Idade}, {copiaDep.Idade}");
            dep.Nome = "Jose";
            copiaDep.Idade = 30;

            Console.WriteLine($"{dep.Nome}, {copiaDep.Nome}");
            Console.WriteLine($"{dep.Idade}, {copiaDep.Idade}");

        }

    }
}
