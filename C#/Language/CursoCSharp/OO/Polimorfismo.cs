using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CursoCSharp.OO
{

    public class Comida {
        public double PesoComida;

        public Comida(double peso) {
            PesoComida = peso;
        }

        public Comida() { }
    }

    public class Feijao : Comida {
        public Feijao(double peso) : base(peso) { 
        
        }

    }

    public class Arroz : Comida
    {

    }

    public class Carne : Comida
    {

    }

    public class Pessoa {
        public double PesoPessoa;

        //public void Comer(Feijao feijao) {
        //    Peso += feijao.Peso;
        //}

        //public void Comer(Arroz arroz)
        //{
        //    Peso += arroz.Peso;
        //}

        //public void Comer(Carne carne)
        //{
        //    Peso += carne.Peso;
        //}

        public void Comer(Comida comida)
        {
            PesoPessoa += comida.PesoComida;

        }

    }

    class Polimorfismo
    {
        public static void Executar() {
            //Settar o peso da comida no contrutor
            Feijao ingred1 = new Feijao(0.3);
            Arroz ingred2 = new Arroz();
            Carne ingred3 = new Carne();

            ingred2.PesoComida = 0.5;
            ingred3.PesoComida = 0.6;


            Pessoa gordo = new Pessoa();

            gordo.PesoPessoa = 120;
            gordo.Comer(ingred1);
            gordo.Comer(ingred2);
            gordo.Comer(ingred3);

            Console.WriteLine(gordo.PesoPessoa);


        }

    }
}
