using System;
using System.Collections.Generic;
using System.Collections;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CursoCSharp.Colecoes
{
    class ColecoesQueue
    {
        public static void Executar() {
            //Esse queue utiliza o import System.Collections.Generic;
            var fila = new Queue<String>();

            fila.Enqueue("Pedro");
            fila.Enqueue("Jaque");
            fila.Enqueue("Yago");

            Console.WriteLine(fila.Peek());
            Console.WriteLine(fila.Count());

            Console.WriteLine(fila.Dequeue());
            Console.WriteLine(fila.Count());

            foreach (var pessoa in fila) {
                Console.WriteLine(pessoa);
            }

            //Esse import utiliza o System.Collections;
            var salada = new Queue();
            salada.Enqueue(3);
            salada.Enqueue("Pedro");
            salada.Enqueue(true);

            Console.WriteLine(salada.Contains(3));
            Console.WriteLine(salada.Contains("pedro"));

        }
    }
}
