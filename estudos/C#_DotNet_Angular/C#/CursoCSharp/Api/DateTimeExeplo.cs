using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CursoCSharp.Api
{
    class DateTimeExeplo
    {

        public static void Executar() {

            var datetime = new DateTime(2021, 12, 15, 12, 34, 54);
            Console.WriteLine(datetime);
            Console.WriteLine(datetime.Day);
            Console.WriteLine(datetime.Month);
            Console.WriteLine(datetime.Year);
            Console.WriteLine(DateTime.Today);

        }

    }
}
