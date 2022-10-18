using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CursoCSharp.OO
{

    interface OperacaoBinaria {
        //Os metodos de uma interface são por padrão public e não podem ser abstract
        // e em sua declaração eu apenas defino o nome, parametros e o tipo de retorno
        // mas não implemento nada.
        int Operacao(int a, int b);
    }

    class Soma : OperacaoBinaria {
        public int Operacao(int a, int b) {
            return a + b;
        }
    }

    class Multi : OperacaoBinaria {
        public int Operacao(int a, int b) {
            return a * b;
        }
    }

    class Subtracao : OperacaoBinaria
    {
        public int Operacao(int a, int b)
        {
            return a - b;
        }
    }

    class Calculadora
    {
        List<OperacaoBinaria> operacoes = new List<OperacaoBinaria>
            {
                new Soma(),
                new Multi(),
                new Subtracao()
            };

        public string ExecutarOperacao(int a, int b) {

            string resultado = "";

            foreach (var op in operacoes) {
                resultado += $"Usando {op.GetType().Name} = {op.Operacao(a, b)}\n";
            }

            return resultado.ToString();
        }
    }

    class InterfaceExemplo
    {

        public static void Executar() {
            Calculadora c = new Calculadora();

            Console.WriteLine(c.ExecutarOperacao(2, 3));

        }
    }
}
