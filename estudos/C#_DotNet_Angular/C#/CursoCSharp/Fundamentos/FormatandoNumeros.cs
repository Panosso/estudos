using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CursoCSharp.Fundamentos
{
	class FormatandoNumeros
	{
		public static void Executar() {
			double valor = 15.17815;
			//Formata o valor para 3 casas decimais
			Console.WriteLine(valor.ToString("F3"));

			//Formata o valor para o valor de uma Moeda
			Console.WriteLine(valor.ToString("C"));

			//Formata o valor para o valor de uma Porcentagem
			Console.WriteLine(valor.ToString("P"));

			////Formata o valor para o valor de uma mascara
			Console.WriteLine(valor.ToString("#.##"));

			//Tranforma o programa em cultura ingles, ou seja, utiliza padroes americanos.
			System.Globalization.CultureInfo culture = new System.Globalization.CultureInfo("en-US");
			Console.WriteLine(valor.ToString("C0", culture));

			int inteiro = 256;

			//Adiciona 0's até que o numero contenha a quantidade de posições de D, no exemplo, ela irá adicionar 7 zeros.
			Console.WriteLine(inteiro.ToString("D10"));
		}
	}
}
