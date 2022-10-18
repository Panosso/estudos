using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CursoCSharp.Excepts
{
    class ExceptTreatment
    {

        public class Conta {

            double Saldo;

            public Conta(double Saldo) {
                this.Saldo = Saldo;
            }

            public void Sacar(double valor) {
                
                if (valor > Saldo) {
                    throw new ArgumentException("Saldo Insuficiente");
                }

                this.Saldo -= valor;

            }
        }

        public static void Executar() {

            var conta = new Conta(1000.00);

            try
            {

                conta.Sacar(100);
                Console.WriteLine("Retirada com sucesso");

            }
            catch (Exception ex)
            {
                Console.WriteLine(ex);
            }
            finally {
                Console.WriteLine("Obrigado");
            }

        }

    }
}
