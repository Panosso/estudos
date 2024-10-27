using System;

namespace Encapsulamento
{
    public class SubCelebridade
    {
        // Todos podem acessar
        public string InfoPublica = "Tenho insta";

        //Herança
        protected string CorOlhos = "Verde";

        // memso projeto
        internal ulong NumeroCelular = 5516997811313;

        //heranca ou mesmo projeto
        protected internal string JeitoDeFalar = "Uso muita girias";

        //mesma class ou herança no mesmo projeto (C# >= 7.2)
        private protected string SegredoFamilia = "Bla Bla";

    }
}
