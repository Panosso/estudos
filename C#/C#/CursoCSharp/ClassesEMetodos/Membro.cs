using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CursoCSharp.ClassesEMetodos
{
	class Membro
	{
		public static void Executar() {
			Pessoa pedro = new Pessoa();
			pedro.Nome = "Pedro";
			pedro.Idade = 30;

			string apresentacao = pedro.Apresentar();
			Console.WriteLine(apresentacao);
			pedro.Apresentacao();

		}
	}
}
