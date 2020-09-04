using System;

namespace _5._Condicionales
{
    class Program
    {
        static void Main(string[] args)
        {
            int x,y;
            string entrada;
            Console.WriteLine("ingrese un numero: ");
            entrada = Console.ReadLine();
            x = Convert.ToInt32(entrada);
            Console.WriteLine("ingrese un numero: ");
            entrada = Console.ReadLine();
            y = Convert.ToInt32(entrada);
            if (x > y)
            {
                Console.WriteLine("{0} > {1}", x, y);
            }
            else
            {
                Console.WriteLine("{0} > {1}", y, x);
            }
            string t = "19.56";
            float tf = float.Parse(t);
            Console.WriteLine("{0}", tf);
            Console.ReadKey();
        }
    }
}
