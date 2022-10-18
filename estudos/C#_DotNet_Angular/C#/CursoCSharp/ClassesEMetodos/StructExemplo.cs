using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CursoCSharp.ClassesEMetodos
{

    interface Ponto {
        void MoverNaDiagonal(int delta);
    }

    struct Coordenada : Ponto {
        public int X;
        public int Y;

        public Coordenada(int x, int y) {
            X = x;
            Y = y;
        }

        public void MoverNaDiagonal(int delta) {
            X += delta;
            Y += delta;
        }

    }

    class StructExemplo
    {

        public static void Executar() {
            
            Coordenada coordenadaInicial;
            
            coordenadaInicial.X = 2;
            coordenadaInicial.Y = 2;

            var coordenadaFinal = new Coordenada(x: 9, y: 1);
            coordenadaFinal.MoverNaDiagonal(10);
            Console.WriteLine(coordenadaFinal.X);
            Console.WriteLine(coordenadaFinal.Y);

        }
    }
}
