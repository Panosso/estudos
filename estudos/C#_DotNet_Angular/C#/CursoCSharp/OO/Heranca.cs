using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CursoCSharp.OO
{
    public class Carro {
        protected readonly int VelocidadeMax;
        int VelocidadeAtual;

        public Carro(int velocidadeMax)
        {
            VelocidadeMax = velocidadeMax;

        }


        protected int AlterarVelocidade(int delta) {
            int novaVelocidade = VelocidadeAtual + delta;

            if (novaVelocidade < 0)
            {

                VelocidadeAtual = 0;
            }
            else if (novaVelocidade > VelocidadeMax)
            {
                VelocidadeAtual = VelocidadeMax;
            }
            else {
                VelocidadeAtual = novaVelocidade;
            }

            return VelocidadeAtual;

        }

        // Com o modificador virtual, o método pode ser sobreescrito
        public virtual int Acelerar() {
            return AlterarVelocidade(5);
        }

        public int Freiar()
        {
            return AlterarVelocidade(-5);
        }

    }

    public class Uno : Carro {

        //Esse base é o contrututor da class Carro  public Carro(int velocidadeMax)
        public Uno() : base(200)
        {


        }
    }

    public class Ferrari : Carro {
        public Ferrari() : base(350) { 

        }

        public override int Acelerar() {
            return AlterarVelocidade(15);
        }

        public new int Freiar() {
            return AlterarVelocidade(-15);
        }

    }

    class Heranca
    {
        public static void Executar() {

            Console.WriteLine("Uno...");
            Uno c1 = new Uno();

            Console.WriteLine(c1.Acelerar());
            Console.WriteLine(c1.Acelerar());
            Console.WriteLine(c1.Freiar());
            Console.WriteLine(c1.Freiar());
            Console.WriteLine(c1.Freiar());

            Console.WriteLine("Ferrari...");
            Ferrari c2 = new Ferrari();

            Console.WriteLine(c2.Acelerar());
            Console.WriteLine(c2.Acelerar());
            Console.WriteLine(c2.Acelerar());
            Console.WriteLine(c2.Acelerar());
            Console.WriteLine(c2.Acelerar());
            Console.WriteLine(c2.Acelerar());

            Console.WriteLine(c2.Freiar());
            Console.WriteLine(c2.Freiar());
            Console.WriteLine(c2.Freiar());
            Console.WriteLine(c2.Freiar());
            Console.WriteLine(c2.Freiar());

        }

        
    }
}
