using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CursoCSharp.ClassesEMetodos
{
	public class CalculadoraEstatica {
		//Para acessar esse método não é necessário criar um objeto, pois esse metodo deixa de pertencer a classe.
		public static int Multi(int a, int b) {
			return a * b;
		}

		// Metodo da classe.
		public int Somar(int a, int b)
		{
			return a * b;
		}
	}

	class MetodosEstaticos
	{
		public static void Executar() {
			int conta = CalculadoraEstatica.Multi(2, 3);
			CalculadoraEstatica c = new CalculadoraEstatica();

			Console.WriteLine(conta);
			Console.WriteLine(c.Somar(2, 3));
		}
	}
}
