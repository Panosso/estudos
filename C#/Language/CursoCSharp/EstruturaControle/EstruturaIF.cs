using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CursoCSharp.EstruturaControle
{
	class EstruturaIF
	{
		public static void Executar() {
			int nota = 0;
			int nota2 = 0;
			double notaAprovado = 10;
			bool comportamento = true;

			// Quando não tiver as chaves, o C# vai entender que a linha logo abaixo o if é o retorno da função
			if (notaAprovado >= nota)
				Console.WriteLine("Aprovado");

			if (notaAprovado >= nota) {
				Console.WriteLine("Aprovado");
				Console.WriteLine("Novamente, vc é foda.");

			}

			if (!comportamento) {
				Console.WriteLine("Aluno com mau comportamento");
			}

			// Caso a nota seja igual a 10 OU 11 comportamento recebera True
			comportamento = nota == 10 || nota == 11;
			Console.WriteLine(comportamento);

			if (nota > 100)
			{
				Console.WriteLine("Nota muito BOA!!!!");
			}
			else if (nota < 10 || nota > 7) {
				Console.WriteLine("Vai levar apenas 10 chineladas!!!!");
			}
			else
			{
				Console.WriteLine("AHHHHHHHHHH MULKEEEEEEEE");
			}

			switch (nota) {
				case 0:
					Console.WriteLine("pessimo");
					break; ;

				case 1:
					Console.WriteLine("aceitavel");
					break;

				default:
					Console.WriteLine("Caso nao seja um valor valido para os cases, cairá nessa parte do cód");
					break;
			}

			while (nota < 7) {
				Console.WriteLine(nota);
				nota += 1;
			}

			do
			{
				Console.WriteLine(nota2);
				nota2 += 1;
			} while (nota2 < 7);

			for (int i = 0; i < 10; i++) {
				Console.WriteLine($"O valor de i é {i}");
			}

			var palavra = new String[] { "pedro", "Jaque", "Yago"};

			foreach (var letra in palavra) {
				Console.WriteLine(letra);
				if (letra == "Jaque") {
					break;
				}
			}

			for (int i = 1; i < 50; i++) {
				if (i % 2 == 1) {
					continue;
				}

				Console.WriteLine(i);
			}

		}
	}
}
