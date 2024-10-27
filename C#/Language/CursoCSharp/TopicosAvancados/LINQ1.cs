using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CursoCSharp.TopicosAvancados
{
    class LINQ1
    {

        public class Aluno {
            public string Nome;
            public int Idade;
            public double Nota;
        }

        public static void Executar() {

            var alunos = new List<Aluno> {
                new Aluno() { Nome = "Pedro", Idade = 29, Nota = 9.9},
                new Aluno() { Nome = "Yago", Idade = 29, Nota = 9.9},
                new Aluno() { Nome = "Jaque", Idade = 34, Nota = 10},
                new Aluno() { Nome = "Ana", Idade = 22, Nota = 5.6},
                new Aluno() { Nome = "Mosart", Idade = 26, Nota = 8.9},
                new Aluno() { Nome = "Matheus", Idade = 24, Nota = 1.5}
            };

            Console.WriteLine("== Aprovado ========");
            var aprovados = alunos.Where( a => a.Idade > 24).OrderBy(a => a.Nome);
            foreach (var aluno in aprovados) {
                Console.WriteLine(aluno.Nome);
            }

            var chamada = alunos.OrderBy(a => a.Nome).Select(a => a.Nome);
            foreach (var aluno in chamada) {
                Console.WriteLine(aluno);
            }

            var alunosPorIdade = from aluno in alunos where aluno.Nota >= 7 orderby aluno.Idade select aluno.Nome;

            Console.WriteLine("\n\n");

            foreach (var aluno in alunosPorIdade) {
                Console.WriteLine(aluno);
            }

        }

    }
}
