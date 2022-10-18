using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CursoCSharp.Fundamentos
{
	class LendoDados
	{
		public static void Executar() {
			Console.WriteLine("Qual seu nome");
			string nome = Console.ReadLine();

			Console.WriteLine("Qual a sua idade?");
			int idade = int.Parse(Console.ReadLine());

			Console.WriteLine("Qual Seu salario?");
			//Ignora a formatação do windows e coloca a padrao do C#
			float salario = float.Parse(Console.ReadLine(), System.Globalization.CultureInfo.InvariantCulture);

			Console.WriteLine($"{nome} {idade} {salario}");
		}
	}
}
