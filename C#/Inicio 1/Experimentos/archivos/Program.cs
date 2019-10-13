using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

namespace archivos
{
    class Program
    {
        static void Main(string[] args)
        {
            
            TextWriter archivo;
            archivo = new StreamWriter("uno.txt");
            string mensaje;
            Console.WriteLine("Ingrese algo:\n");
            mensaje = Console.ReadLine();
            archivo.WriteLine(mensaje);
            archivo.Close();
            //Console.Clear();
            
            

            TextReader leer_archivo;
            leer_archivo = new StreamReader("uno.txt");
            Console.WriteLine("tu ingresaste lo sgt:\n");
            Console.WriteLine(leer_archivo.ReadToEnd());
            leer_archivo.Close();
            Console.WriteLine("tambien se creo un archivo de texto llamado uno.txt");
            Console.WriteLine("el cual tiene escrito lo que acabas de ingresar");
            Console.ReadKey();


        }
    }
}
