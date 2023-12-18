using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CursoCSharp.Colecoes
{
    class DicionarioExemplo
    {
        public static void Executar() {
            //Trabalha com Chave e valor.
            var filme = new Dictionary<int, string>();

            filme.Add(1, "Viagem");
            filme.Add(2, "Teste");
            filme.Add(3, "Porn");

            Console.WriteLine(filme.ContainsKey(2));

            foreach (var item in filme) {
                Console.WriteLine(item);
            }

            filme.TryGetValue(2, out string filmeTeste);
            Console.WriteLine(filmeTeste);

            foreach (KeyValuePair<int, string> f in filme) {
                Console.WriteLine(f.Value);
                Console.WriteLine(f.Key);
            }

            foreach (var f in filme)
            {
                Console.WriteLine(f.Key);
                Console.WriteLine(f.Value);
            }
        }

    }
}
