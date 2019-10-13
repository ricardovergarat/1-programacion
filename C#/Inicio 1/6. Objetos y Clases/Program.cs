using System;

namespace _6._Objetos_y_Clases
{
    class Program
    {
        static void Main(string[] args)
        {
            Empleados un_empleado;
            un_empleado = new Empleados();
            un_empleado.edad = 25;
            un_empleado.Nombre = "hugito";
            un_empleado.sueldo = 12.5m;
            Decimal total;
            total = un_empleado.calcular_saldo(30);
            Console.WriteLine("el empleado " + un_empleado.Nombre);
            Console.WriteLine("el total es: {0}", total);
            Console.ReadKey();
        }
    }
}
