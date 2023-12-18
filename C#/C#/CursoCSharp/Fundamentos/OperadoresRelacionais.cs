using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CursoCSharp.Fundamentos
{
	class OperadoresRelacionais
	{
		public static void Executar() {
			double nota = 2.0;
			double notaDeCorte = 7.0;
			// Valida se o valor de 'nota' é maior ou igual a 6, caso seja então a variavel resultado recebera Aprovado, caso contrário recebera o valor Reprovado.
			string resultado = nota >= 6.0 ? "Aprovado" : "Reprovado";

			Console.WriteLine($"Nota invalida {nota > 10.0}");
			Console.WriteLine($"Nota invalida {nota < 0.0}");
			Console.WriteLine($"Nota invalida {nota == 6.0}");
			Console.WriteLine($"Nota invalida {nota != 10.0}");
			Console.WriteLine($"Nota invalida {resultado}");


		}
	}
}
