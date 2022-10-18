using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CursoCSharp.Excepts
{

    public class NegativoException2 : Exception {

        public NegativoException2() { }

        public NegativoException2(string message) : base(message) { }

        public NegativoException2(string message, Exception inner) : base(message, inner) { }

    }

    public class ImparException : Exception {
        public ImparException(string message) : base(message) { }
    }


    class ExcecoesPersolnalizadas
    {

        public static int PositivoPar() {

            Random random = new Random();

            int valor = random.Next(-30, 30);

            if (valor < 0)
            {
                throw new NegativoException2("Numero negativo: " + valor);
            }
            else if (valor % 2 != 0)
            {
                throw new ImparException("Numero impar: " + valor);
            }
            else {
                return valor;
            }

        }

        public static void Executar()
        {
            try
            {

                Console.WriteLine(PositivoPar());
            }
            catch (NegativoException2 ex)
            {
                Console.WriteLine(ex);
            }
            catch (ImparException ie)
            {
                Console.WriteLine(ie);
            }
            catch (Exception exe)
            {
                Console.WriteLine("Erro nao tratado.");
            }
            finally {
                Console.WriteLine("Finalizado");
            }
        }

    }
}
