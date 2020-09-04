using System;
using System.Collections.Generic;

namespace zona_de_pruebas
{
    class Program
    {

        static int[] obtener_indice_diagnostico(int a, int b, int c)
        {
            int[] numeros = new int[c];
            numeros[0] = a;
            numeros[1] = b;
            return numeros;
            
        }

        static List<int> obtener_lista(int a,int b, int c)
        {
            List<int> datos = new List<int>();
            datos.Add(a);
            datos.Add(b);
            datos.Add(c);
            return datos;
        }

        static void Main(string[] args)
        {
            int[] indices = obtener_indice_diagnostico(2,4,2);
            List<int> mi_lista = obtener_lista(2, 5, 6);
            Console.WriteLine(mi_lista[0]);
            
            /*
            bool p = true;
            for ( int i = 0; i < texto.Length; i++){
                Console.WriteLine(texto[i]);
                bool q = char.IsNumber(texto[i]);
                Console.WriteLine(q);
                p = p && q;
            }
            //int x = Convert.ToInt32(texto);
            //Console.WriteLine(x);
            Console.WriteLine("p es: " + p);
            */
        }

        
    }
}
