using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CursoCSharp.ClassesEMetodos
{
    class DesafioAcessarAtributo
    {

        int Variavel = 10;

        public static void Executar() {
            DesafioAcessarAtributo a = new DesafioAcessarAtributo();
            Console.WriteLine(a.Variavel);
        }
    }
}
