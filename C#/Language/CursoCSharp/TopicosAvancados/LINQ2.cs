using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Linq;
using CursoCSharp.TopicosAvancados;

namespace CursoCSharp.TopicosAvancados
{
    class LINQ2
    {
        public static void Executar()
        {

            var alunos = new List<LINQ1.Aluno> {
                new LINQ1.Aluno() { Nome = "Pedro", Idade = 29, Nota = 9.9},
                new LINQ1.Aluno() { Nome = "Yago", Idade = 29, Nota = 9.9},
                new LINQ1.Aluno() { Nome = "Jaque", Idade = 34, Nota = 10},
                new LINQ1.Aluno() { Nome = "Ana", Idade = 22, Nota = 5.6},
                new LINQ1.Aluno() { Nome = "Mosart", Idade = 26, Nota = 8.9},
                new LINQ1.Aluno() { Nome = "Matheus", Idade = 24, Nota = 1.5}
            };

            var pedro = alunos.First(aluno => aluno.Nome.Equals("Pedr"));
            Console.WriteLine(pedro.Nota);

            var sicrano = alunos.FirstOrDefault(aluno => aluno.Nota.Equals("Fulano"));
            if (sicrano == null) {
                Console.WriteLine("Aluno inexistente");
            }

            var outroPedro = alunos.LastOrDefault(aluno => aluno.Nome.Equals("Pedro"));
            Console.WriteLine(outroPedro.Nota);

            var exemploSkip = alunos.Skip(1).Take(3);
            foreach (var item in exemploSkip) {
                Console.WriteLine(item.Nome);
            }

            var maiorNota = alunos.Max(aluno => aluno.Nota);
            Console.WriteLine(maiorNota);

            var menorNota = alunos.Min(aluno => aluno.Nota);
            Console.WriteLine(maiorNota);










        }

    }
}
