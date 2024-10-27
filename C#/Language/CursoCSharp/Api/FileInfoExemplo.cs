using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

namespace CursoCSharp.Api
{
    class FileInfoExemplo
    {

        public static void Executar() { 
        
            var caminhoOrigem = @"E:\Users\Cesar\Desktop\all_projects\estudos\C#_DotNet_Angular\C#\CursoCSharp\Api\primeiro_arquivo2.txt";
            var caminhoDestino = @"E:\Users\Cesar\Desktop\all_projects\estudos\C#_DotNet_Angular\C#\CursoCSharp\Api\primeiro_arquivo2.txt";
            var caminhoCopia = @"E:\Users\Cesar\Desktop\all_projects\estudos\C#_DotNet_Angular\C#\CursoCSharp\Api\primeiro_arquivo2.txt";

            using (StreamWriter sw = File.CreateText(caminhoOrigem)) {
                sw.WriteLine("Arquivo original");
            }

            FileInfo origem = new FileInfo(caminhoOrigem);
            Console.WriteLine(origem.Name);
            Console.WriteLine(origem.IsReadOnly);
            Console.WriteLine(origem.FullName);
            Console.WriteLine(origem.Extension);

            origem.CopyTo(caminhoCopia);
            origem.MoveTo(caminhoDestino);
        }

    }
}
