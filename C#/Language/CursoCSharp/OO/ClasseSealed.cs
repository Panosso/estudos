using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CursoCSharp.OO
{
    class ClasseSealed
    {

        sealed class SemFilho {
            public double ValorFortuna() {
                return 123321;
            }
        }

        //class SouFilho : SemFilho { 
        //    
        //}

        class Avo {
            public virtual bool HonraFamili() {
                return true;
            }
        }

        class Pai : Avo {
            public sealed override bool HonraFamili()
            {
                return true;
            }
        }

        class FilhoRebelde : Pai {

            //Esse método por ser sealed nao pode ser sobreescrito
            //public override bool HonraFamili() { 

            //}

            //Porém é possivel fazer uma gambiarra
            public new bool HonraFamili() {
                return false;
            }
        }

        public static void Executar() {

            SemFilho semFilho = new SemFilho();
            Console.WriteLine(semFilho.ValorFortuna());

            FilhoRebelde filho = new FilhoRebelde();
            Console.WriteLine(filho.HonraFamili());

        }
    }
}
