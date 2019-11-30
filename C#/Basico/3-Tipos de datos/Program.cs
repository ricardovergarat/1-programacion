using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _3_Tipos_de_datos
{
    class Program
    {
        static void Main(string[] args)
        {
            // recordar que los byte son de 0 a 255
            // en caso de no estar en ese rango el IDE dara un pequeño error
            byte variable = 255;
            Console.WriteLine("El valor de la variable es: " + variable);
            // rango de int -2147.483.648. al 2147.483.648
            int entero = 34;
            Console.WriteLine("El valor del entero es: " + entero);
            Console.WriteLine("Presione una tecla para terminar");
            Console.ReadKey();
        }
    }
}
