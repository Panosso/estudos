using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

namespace CursoCSharp.Api
{
    class LendoArquivo
    {
        public static void Executar() {
            var path = @"E:\Users\Cesar\Desktop\all_projects\estudos\C#_DotNet_Angular\C#\CursoCSharp\Api\primeiro_arquivo2.txt";

            if (!File.Exists(path)) {

                using (StreamWriter sw = File.AppendText(path))
                {
                    sw.WriteLine("Produto;Preço;Qty");
                    sw.WriteLine("Caneta;1.00;3");
                    sw.WriteLine("borracha;3.00;1");

                }

            }

            try {
                using (StreamReader sr = new StreamReader(path)) {
                    var texto = sr.ReadToEnd();
                    Console.WriteLine(texto);
                };

            }
            catch (Exception ex)
            {
                Console.WriteLine("Erro ao ler o arquivo.");
            }
        }

    }
}
