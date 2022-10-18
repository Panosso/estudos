using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CursoCSharp.ClassesEMetodos
{

    public struct SPonto {
        public int X;
        public int Y;
    }

    public class CPonto
    {
        public int X;
        public int Y;
    }

    class StructVSClasses
    {
        public static void Executar() {

            SPonto p1 = new SPonto { X = 1, Y = 3 };
            SPonto cpp1 = p1; //Atribuição por valor, portanto será uma atribuição onde serão gerados 2 endereços de memorias e cada objeto aponta para um endereço.
            p1.X = 3;

            Console.WriteLine($"P1 X: {p1.X}");
            Console.WriteLine($"P1 Copia X: {cpp1.X}");

            CPonto p2 = new CPonto { X = 2, Y = 3 };
            CPonto cpp2 = p2; //Atribuição por referencia, portanto os 2 objetos apontaram para o mesmo endereço de memória, portanto se alterar em um objeto o outro tbm será alterado.
            p2.X = 4;
            Console.WriteLine($"P1 X: {p2.X}");
            Console.WriteLine($"P1 Copia X: {cpp2.X}");

        }

    }
}
