using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CursoCSharp.ClassesEMetodos
{
    class Recursividade
    {
        public static double fatorial(int numero = 0)
        {
            if (numero == 0)
            {
                return 1;
            }
            else
            {
                return numero * fatorial(numero - 1);
            }

        }

        public static void Executar() {
            string numero;
            double resultado;

            Console.WriteLine("Digite o numero positivo maior que 0 que vc quer saber o fatorial");
            numero = Console.ReadLine();
            resultado = fatorial(int.Parse(numero));

            Console.WriteLine(resultado);
        }

    }
}
