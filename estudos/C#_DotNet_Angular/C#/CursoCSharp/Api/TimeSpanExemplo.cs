using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CursoCSharp.Api
{
    class TimeSpanExemplo
    {

        public static void Executar() {
            var intervalo = new TimeSpan(days: 10, hours:20, minutes: 30, seconds: 40);
            Console.WriteLine(intervalo);
        }

    }
}
