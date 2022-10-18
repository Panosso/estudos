using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CursoCSharp.ClassesEMetodos
{
	class Pessoa
	{
		public string Nome;
		public int Idade;

		public string Apresentar() {
			return string.Format($"Ola {Nome} e tenho {Idade}");
		}

		public void Apresentacao() {
			Console.WriteLine($"Ola {Nome} e tenho {Idade}");
		}
	}
}
