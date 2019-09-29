using System;
using System.Collections.Generic;
using System.Text;

namespace _6._Objetos_y_Clases
{
    public class Empleados
    {
        // contructor
        // suele ser donde se inicializan los valores de la clase
        public Empleados()
        {
            Nombre = "";
            sueldo = 0.0m;
            edad = 0;
        }

        // atributos
        public string Nombre;
        public Decimal sueldo;
        public int edad;

        // metodos
        public decimal calcular_saldo(int n_dias)
        {
            return sueldo * n_dias;
        }

    }
}
