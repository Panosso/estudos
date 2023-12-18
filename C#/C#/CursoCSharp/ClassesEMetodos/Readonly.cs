using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CursoCSharp.ClassesEMetodos
{

    public class Cliente {
        public string Nome;

        //Read only, deixa que o atributo receba um valor, porém esse valor para esse objeto criado é imutavel.
        readonly DateTime Nascimento;

        public Cliente(string nome, DateTime nascimento) {
            Nome = nome;
            Nascimento = nascimento;
        }


        public string GetDataNascimento() {
            return String.Format($"{Nascimento.Day}/{Nascimento.Month}/{Nascimento.Year}");
        }
    }

    class Readonly
    {

        public static void Executar() {
            var NovoCliente = new Cliente("Pedro", new DateTime(1991, 12, 15));

            Console.WriteLine(NovoCliente.Nome);
            Console.WriteLine(NovoCliente.GetDataNascimento());
        }
    }
}
