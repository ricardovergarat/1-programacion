using System;

namespace _4._Conversiones_de_tipo
{
    class Program
    {
        static void Main(string[] args)
        {
            string a = ""
            int x = 5;
            Decimal y = 12.1m;
            bool p = false;
            string cadena = string.Empty; // iniciamos una variable de tipo strin vacia
            DateTime fecha = DateTime.MinValue;
            //x = (int)y;
            // x = Convert.ToInt32(p); no da error ya que dara lo sgt false = 0 y true = 1
            // poner un string en convert dara un error(si se ponen letras dara el error)
            // si el string son numero si realizara la convercion
            x = Convert.ToInt32(y);
            Console.WriteLine("x vale: {0}", x);
            Console.WriteLine("y vale: {0:C}", y); // {0:C} agregara un signo de peso ($)
            Console.WriteLine("p vale: " + p.ToString());
            Console.WriteLine("cadena vale: " + cadena);
            Console.WriteLine("fehca vale: " + fecha.ToShortDateString());
            Console.ReadKey();

        }
    }
}
