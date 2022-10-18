using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CursoCSharp.Fundamentos
{
	class NotacaoPonto
	{
		public static void Executar() {
			// O operador . chama os metodos que uma variavel ou objeto tem.
			var saudacao = "ola".ToUpper().Insert(3, " World!").Replace("World", "Mundo");
			Console.WriteLine(saudacao);


			string valorImportante = null;
			// O C# verifica se o valor da variavel está correto, caso nao esteja ele ignora e não mostra o erro.
			Console.WriteLine(valorImportante?.Length);
		}
	}
}
