using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
// nesesitamos agragar esta biblioteca para trabajar con los archivos
using System.IO;

namespace _15_Crear_un_Archivo
{
    class Program
    {
        static void Main(string[] args)
        {
            TextWriter archivo;
            archivo = new StreamWriter("gastos.txt");
            string mensaje;
            mensaje = Console.ReadLine();
            archivo.WriteLine(mensaje);
            archivo.Close();
        }
    }
}
