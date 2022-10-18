using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CursoCSharp.MetodosFuncoes
{
    class DelegateComParametros
    {

        public delegate int Operacao(int x, int y);

        public static int Soma(int x, int y) {
            return x + y;
        }

        public static string Calculadora(Operacao op, int x, int y) {
            var resultado = op(x, y);
            return resultado.ToString();
        }

        public static void Executar() {

            Operacao sub = (int x, int y) => x - y;
            Console.WriteLine(Calculadora(sub, 10, 5));

            Console.WriteLine(Calculadora(Soma, 3, 2));

        }

    }
}
