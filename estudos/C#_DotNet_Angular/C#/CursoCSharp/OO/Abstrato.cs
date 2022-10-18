using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CursoCSharp.OO
{
    //Classes abstratas nao estão completas, portanto qualquer classe não abstrata precisa completar as metodos.
    class Abstrato
    {

        // Os metodos de uma classe de uma classe abstrata não precisam ser do tipo abstract
        public abstract class Celular {
            public abstract string Assitente();

            public string Tocar() {
                return "Trim Trim";
            }


        }

        public class Sansung : Celular {
            public override string Assitente()
            {
                return "Olá, meu nome é Bixby!";

                throw new NotImplementedException();
            }
        }

        public class IPhone : Celular {
            public override string Assitente()
            {
                return "Olá, sou a Siri";

                throw new NotImplementedException();
            }
        }


        public static void Executar() {
            //Classes abstratas não podem ser instanciadas
            //Celular c = new Celular();

            var celulares = new List<Celular> {
            new IPhone(),
            new Sansung()
            };

            foreach (var cel in celulares)
            {
                Console.WriteLine(cel.Assitente());

            };


        }
    }
}
