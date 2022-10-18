using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CursoCSharp.MetodosFuncoes
{
    class DelegateLambda
    {

        //Cria uma assinatura para a função
        delegate double Operacao(double x, double y);

        public static void Executar() {

            Operacao sum = (x, y) => x + y;

            Console.WriteLine(sum(10, 20));

        }
    }
}
