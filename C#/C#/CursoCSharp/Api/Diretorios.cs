using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

namespace CursoCSharp.Api
{
    class Diretorios
    {

        public static void Executar() {

            var NovoDir = @"E:\Users\Cesar\Desktop\all_projects\estudos\C#_DotNet_Angular\C#\CursoCSharp\Api\teste";
            var NovoDirDestino = @"E:\Users\Cesar\Desktop\all_projects\estudos\C#_DotNet_Angular\C#\CursoCSharp\Api\teste";
            var dirProjeto = @"E:\Users\Cesar\Desktop\all_projects\estudos\C#_DotNet_Angular\C#\CursoCSharp\Api\teste";


            if (Directory.Exists(NovoDir))
            {
                Directory.Delete(NovoDir, true);
            }

            if (Directory.Exists(NovoDirDestino))
            {
                Directory.Delete(NovoDirDestino, true);
            }

            Directory.CreateDirectory(NovoDir);
            Console.WriteLine(Directory.GetCreationTime(NovoDir));

            Console.WriteLine("== Pastas ============");
            var pastas = Directory.GetDirectories(dirProjeto);
            foreach (var pasta in pastas) {
                Console.WriteLine(pasta);
            }


        }
    }
}
