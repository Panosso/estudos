using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

namespace CursoCSharp.Api
{

    public static class ExtensaoString
    {
        public static string ParseHome(this string path)
        {
            string home = Environment.ExpandEnvironmentVariables("%HOMEDRIVE%HOMEPATH%");

            return path.Replace("~", home);
        }
    }

    class PrimeiroArquivo
    {

        public static void Executar() {

            var path = @"E:\Users\Cesar\Desktop\all_projects\estudos\C#_DotNet_Angular\C#\CursoCSharp\Api\primeiro_arquivo2.txt";

            if (!File.Exists(path)) {
                Console.WriteLine("Entrei no file");
                using (StreamWriter sw = File.CreateText(path)) {

                    sw.WriteLine("Esse é o");
                    sw.WriteLine("Primeiro arquivo em C#");
                }
            }

            using (StreamWriter sw = File.AppendText(path)) {
                sw.WriteLine("Mais uma linha escrita.");
            }
        }

    }
}
