using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CursoCSharp.Fundamentos
{
	class Conversoes
	{
		public static void Executar() {
			int inteiro = 10;
			double quebrado = inteiro;
			Console.WriteLine(quebrado);

			double nota = 9.7;
			int notaTruncada = (int) nota;
			Console.WriteLine($"Idade inserida: {notaTruncada}");

			Console.WriteLine("Digite a sua idade");
			string idadeString = Console.ReadLine();
			int idadeInteiro = int.Parse(idadeString);
			idadeInteiro = Convert.ToInt32(idadeString);
			Console.WriteLine($"Resultado: {idadeInteiro}");

			Console.WriteLine("Digite um numero");
			//Faz de forma segura a conversao dos dados.
			int.TryParse(Console.ReadLine(), out int numero);
			Console.WriteLine($"Resultado: {numero}");
		}
	}
}
