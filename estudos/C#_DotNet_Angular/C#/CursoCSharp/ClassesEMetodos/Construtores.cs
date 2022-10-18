using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CursoCSharp.ClassesEMetodos
{
	class Carro {
		public string Modelo;
		public string Fabricante;
		public int Ano;

		public Carro(string modelo, string fabricante, int ano) {
			this.Modelo = modelo;
			this.Fabricante = fabricante;
			this.Ano = ano;
		}

		public Carro() { 
		
		}

		public string Apresentacao() {
			return string.Format($"Esse é o carro: {this.Modelo} do fabricante {this.Fabricante} ano {this.Ano}");
		}
	}
	class Construtores
	{

		public static void Executar() {

			var carro = new Carro();
			carro.Fabricante = "BMW";
			carro.Ano = 1950;
			carro.Modelo = "325i";
			Console.WriteLine(carro.Apresentacao());

			var carro1 = new Carro("BMW", "Ford", 1975);
			Console.WriteLine(carro1.Apresentacao());

			var carro2 = new Carro()
			{
				Fabricante = "Ford",
				Modelo = "Uno",
				Ano = 2019
			};
			Console.WriteLine(carro2.Apresentacao());
		}
	}
}
