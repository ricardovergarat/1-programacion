using System;

namespace _3._Tipos_de_Datos
{
    class Program
    {
        static void Main(string[] args)
        {
            int x = 0;
            float y = 1.5f; // los flotantes de siempre
            double d = 1.50;     // son flotantes con mas decimales
            string una_cadena = "esto esta muy aburrido";
            bool p = true; // estas son variables de tipo booleano
            DateTime fecha = DateTime.MinValue;
            Console.WriteLine("el valor de x es: {0}", x); // asi se puede poner valores en consola
            Console.WriteLine("el valor de y es : {0}", y);
            Console.WriteLine("elvalor de d es: {0}", d);
            Console.WriteLine("el valor de una_cadea es: " + una_cadena);
            Console.WriteLine("el valor de p es: " + p.ToString()); // nombre variable.toString() ----> convierte a string
            Console.WriteLine("el valor de fecha es: " + fecha.ToShortDateString());
            Console.ReadKey();
        }
    }
}
