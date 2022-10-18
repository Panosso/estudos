using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CursoCSharp.Fundamentos
{
	class VariaveisEConstantes
	{
		public static void Executar() {
			// Area de uma circunferencia
			
			// Variavel com o valor double
			double raio = 4.5;

			// Variavel de valor constante, portanto nao pode ser alterado pelo programa
			const double PI = 3.15;

			// Variavel booleana
			bool estaChovendo = true;

			//Equivalente ao int, porém apenas valores positivos
			byte idade = 45;

			//Equivalente ao int
			sbyte saldoGols = sbyte.MinValue;

			// Equivalente ao int
			short salario = short.MaxValue;

			// Valor inteiro
			int menorValor = int.MinValue;

			// Valor inteiro maior
			uint popBR = uint.MaxValue;

			//Valores grandes
			long popAmerica = long.MaxValue;

			// Valores MUITO grandes
			ulong popMundial = ulong.MaxValue;

			// Precisa ter esse f no final para ser do tipo float
			float precoPC = 1299.99f;

			//Pode colocar esses '_' que serão ignorados na hora de ler o numero
			double valorApple = 1_000_000_000_000;

			// Apenas um char
			char abc = 'a';

			// String
			string frase = "O rato roeu a roupa do rei de roma";

			Console.WriteLine(raio);
			Console.WriteLine("idade " + idade);
			Console.WriteLine("idade 2" + menorValor);
			Console.WriteLine("Saldo Gols " + saldoGols);
			Console.WriteLine("popBR " + popBR);
			Console.WriteLine("popAmerica " + popAmerica);
			Console.WriteLine("popMundial " + popMundial);
			Console.WriteLine("precoPC " + precoPC);
			Console.WriteLine("valorApple " + valorApple);
			Console.WriteLine("abc " + abc);
			Console.WriteLine("frase " + frase);

		}

	}
}
