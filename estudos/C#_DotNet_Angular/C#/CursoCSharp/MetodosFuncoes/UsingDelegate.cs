using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CursoCSharp.MetodosFuncoes
{
    class UsingDelegate
    {

        delegate double Soma(double a, double b);
        delegate void ImprimirSoma(double a, double b);

        static double MinhaSoma(double x, double y) {
            return x + y;
        }

        static void MeuImprimirSoma(double a, double b) {
            Console.WriteLine(a + b);
        }

        public static void Executar() {
            Soma op1 = MinhaSoma;
            op1(5, 6);

            ImprimirSoma op2 = MeuImprimirSoma;
            op2(10, 20);

            Func<double, double, double> Somatorio = MinhaSoma;
            Console.WriteLine(Somatorio(7, 8));

            Action<double, double> op4 = MeuImprimirSoma;
            op4(9, 10);

        }

    }
}
