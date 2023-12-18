using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CursoCSharp.MetodosFuncoes
{

    public static class ExtensoesInteiro
    {
        public static int Soma(this int num, int outroValor)
        {
            return num + outroValor;
        }

        public static int Subtracao(this int num, int outroNumero)
        {
            return num - outroNumero;
        }

        public static double Divisao(this double num, double outroNumero)
        {
            return num / outroNumero;
        }

    }

    class MetodoExtensao
    {
        public static void Executar() {
            int inteiro = 5;
            double valores = 10;


            Console.WriteLine(inteiro.Soma(3));
            Console.WriteLine(inteiro.Subtracao(5));
            Console.WriteLine(valores.Divisao(2));
        }

    }
}
