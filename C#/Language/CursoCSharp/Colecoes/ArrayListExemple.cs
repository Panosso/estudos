using System;
using System.Collections;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CursoCSharp.Colecoes
{
    class ArrayListExemple
    {
        public static void Executar() {

            var arraylist = new ArrayList {
                "Palvra",
                3,
                true,
                5.9
            };

            arraylist.Add(3.14);

            foreach (var item in arraylist) {
                Console.WriteLine(item.GetType());
                Console.WriteLine(item);
            }

        }
    }
}
