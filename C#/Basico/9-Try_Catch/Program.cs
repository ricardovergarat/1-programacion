using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

// esto es similar a un try en python es decir para evitar errores

    /*
     su syntasis es:

    try
    {

    }
    catch(Exception error)
    {

    }

     */

namespace _9_Try_Catch
{
    class Program
    {
        static void Main(string[] args)
        {
            double precio , total;
            int cantidad;

            try
            {
                Console.WriteLine("catidad: ");
                cantidad = Convert.ToInt16(Console.ReadLine());
                Console.WriteLine("Precio: ");
                precio = Convert.ToDouble(Console.ReadLine());
                total = cantidad * precio;
                Console.WriteLine("El total es: " + total);
                Console.WriteLine("Presione una tecla para terminar");
                Console.ReadKey();


            }
            catch(Exception error)
            {
                Console.WriteLine("No se ingreso un numero y dio un error");
                Console.ReadKey();
            }
            

        }
    }
}
