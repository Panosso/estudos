using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CursoCSharp.ClassesEMetodos
{
	class CalculadoraComun {

		public string Conta(int a, int b, string operacao) {
			dynamic resultado;

			switch (operacao) {
				case "soma":
					resultado = a + b;
					break;

				case "subtracao":
					resultado = a - b;
					break;

				case "multiplicacao":
					resultado = a * b;
					break;

				case "divisao":
					resultado = a / b;
					break;

				default:
					resultado = "nenhuma operacao válida";
					break;
			}


			return string.Format($"{resultado}");
		}
	}

	public class CalculadoraCadeia{
		int memoria;
		//Será retornado a instancia atual do objeto atraves da palavra this.
		public CalculadoraCadeia Somar(int a) {
			memoria += a;
			return this;
		}

		public int Resultado() {
			return memoria;
		}

		public CalculadoraCadeia Zerar() {
			memoria = 0;
			return this;
		}
	}

	class MetodosComRetorno {
		public static void Executar() {
			CalculadoraComun c = new CalculadoraComun();
			Console.WriteLine(c.Conta(10, 20, "multiplicacao"));

			CalculadoraCadeia cc = new CalculadoraCadeia();
			cc.Somar(3);
			cc.Somar(3);
			cc.Somar(3);
			cc.Somar(3);
			Console.WriteLine(cc.Resultado());
			cc.Zerar();
			cc.Somar(4);
			Console.WriteLine(cc.Resultado());

		}
	}
}
