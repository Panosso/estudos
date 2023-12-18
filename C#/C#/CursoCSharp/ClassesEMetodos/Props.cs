using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CursoCSharp.ClassesEMetodos
{


    public class CarroOpcional {
        double desconto = 0.1;
        string nome;
        public string Nome { 
            get
            {
                return "Opcional: " + nome;
            }
            set {
                nome = value;
            }
        }

        //Ja cria os métodos get e set da propriedade, no exemplo Preco
        public double Preco { get; set; }

        //Cria o método get realizando o calculo
        public double PrecoComDesconto {
            get => Preco - (desconto * Preco);
        }

        public CarroOpcional() { 
        
        }

        public CarroOpcional(string nome, double preco)
        {
            this.nome = nome;
            Preco = preco;

        }

    }

    class Props
    {

        public static void Executar() {

            var op1 = new CarroOpcional("Ar condicionado", 1000);
            Console.WriteLine(op1.PrecoComDesconto);
            Console.WriteLine(op1.Nome);
            op1.Nome = "Seta";
            Console.WriteLine(op1.Nome);
        }
    }
}
