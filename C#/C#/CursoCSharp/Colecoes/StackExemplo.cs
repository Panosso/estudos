using System;
using System.Collections;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CursoCSharp.Colecoes
{
    class StackExemplo
    {

        public static void Executar() {
            var pilha = new Stack();

            pilha.Push(3);
            pilha.Push("fgdsah");
            pilha.Push(true);
            pilha.Push(3.14f);

            foreach (var item in pilha)
            {
                Console.WriteLine(item);

            }

            //remove o ultimo elemento adicionado.
            Console.WriteLine(pilha.Pop());

            foreach (var item in pilha)
            {
                Console.WriteLine(item);

            }

        }

    }
}
