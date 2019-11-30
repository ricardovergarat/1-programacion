using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

namespace _16_Leer_un_Archivo
{
    class Program
    {
        static void Main(string[] args)
        {
            TextReader archivo;
            archivo = new StreamReader("gastos.txt");
            string datos;
            datos = archivo.ReadToEnd();
            Console.WriteLine(datos);
            int x = 0;
            while (archivo.ReadLine() != archivo.ReadToEnd)
            {
                Console.WriteLine(x);
            }
            Console.ReadKey();
            archivo.Close();
        }
    }
}
