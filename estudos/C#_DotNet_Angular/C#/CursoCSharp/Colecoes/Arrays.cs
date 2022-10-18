using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CursoCSharp.Colecoes
{
    class Arrays
    {
        public static void Executar()
        {
            //Deve ser armazenado os valores de acordo com o tipo do array, nesse exmplo será apenas string e ele possui um tamanho fixo.
            string[] alunos = new string[5];

            alunos[0] = "Pedro";
            alunos[1] = "Yago";
            alunos[2] = "Jaque";
            alunos[3] = "Jose";
            alunos[4] = "Tobias";

            foreach (var aluno in alunos) {
                Console.WriteLine(aluno);
            }

            double somatorio = 0;
            double[] notas = { 1, 9.8, 5.9 };

            foreach(var nota in notas)
            {
                somatorio += nota;
            }

            double media = somatorio / notas.Length;
            Console.WriteLine(media);

        }
    }
}
