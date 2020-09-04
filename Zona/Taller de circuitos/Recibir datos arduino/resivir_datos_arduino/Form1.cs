using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Windows.Forms;

// bibliotecas nuevas

namespace resivir_datos_arduino
{
    public partial class Form1 : Form
    {
        // aqui emepezamos en codigo
        System.IO.Ports.SerialPort mi_entrada; // --> declaracion de variable
      
        public Form1()
        {
            InitializeComponent();
            // aqui usamos el controctor
            mi_entrada = new System.IO.Ports.SerialPort();
            mi_entrada.PortName = "COM3"; // --> aqui definimos el puerto
            mi_entrada.BaudRate = 9600; // cuantos baudios de señal
            mi_entrada.ReadTimeout = 500;
            mi_entrada.Open();

        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void escuchar_serial()
        {
            string dato = mi_entrada.ReadLine();
            label_del_arduino.Text = dato;
        }

        private void label_del_arduino_Click(object sender, EventArgs e)
        {
            Thread hilo = new Thread(escuchar_serial);
            hilo.Start();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (label_del_arduino.Text == "label" || label_del_arduino.Text == "ON")
            {
                label_del_arduino.Text = "OFF";
            }
            else {
                label_del_arduino.Text = "ON";
            }
        }
    }
}
