using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CursoCSharp.MetodosFuncoes
{
    class LambdaExecmple
    {
        public static void Executar()
        {
            //Cria uma função onde o retorno dele é void.
            // Action nomeFuncao = (0 ou N variaveis) => {codificacao}
            Action algoConsole = () => {
                Console.WriteLine("Lambda com C#");
            };

            //Cria uma função onde o retorno dele é void, com parametros lembrando que é necessário passar o tipo do parametro, nesse exemplo <string>.
            Action<string> algoConsole2 = (a) => {
                Console.WriteLine("Lambda com C#"+a);
            };

            algoConsole();
            algoConsole2("!!!!!!!!!!!!!!!!!!!");

            //Cria uma função com um obrigatoriamente um tipo de retorno que é o ultimo tipo passado dentro dos <>
            // nesse exemplo, o retorno será do tipo int
            Func<int> jogarDado = () =>
            {
                Random random = new Random();
                return random.Next(1, 7);
            };

            Console.WriteLine(jogarDado());

            //Recebe um parametro do tipo inteiro e obrigatoriamente retorna um tipo string
            // Func<tipoVar1, tipoVar2 ... tipoVarN, tipoRetorno> nomeFuncao = (Var1, Var2, ... VarN) => {Códificação}
            Func<int, string> conversorHex = numero => numero.ToString("X");

            Console.WriteLine(conversorHex(1234));

            //Recebe um parametro do tipo inteiro e obrigatoriamente retorna um tipo string
            // Func<tipoVar1, tipoVar2 ... tipoVarN, tipoRetorno
            Func<int, int, int, string> formatoData = (dia, mes, ano) => 
            String.Format("{0:D2}/{1:D2}/{2:D2}", dia, mes, ano);

            Console.WriteLine(formatoData(1, 1, 2019));

        }

    }
}
