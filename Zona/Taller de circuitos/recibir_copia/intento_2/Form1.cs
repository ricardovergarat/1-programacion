using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

//nueva
using System.IO.Ports;

namespace intento_2
{
    public partial class Ventana : Form
    {
        private SerialPort serialPort1;
        public Ventana()
        {
            InitializeComponent();
            serialPort1 = new SerialPort();
            serialPort1.PortName = "COM3";
            serialPort1.BaudRate = 9600;
            serialPort1.DtrEnable = true;
            serialPort1.Open();
            Console.WriteLine("El primer hola mundo de c#");
            serialPort1.DataReceived += serialPort1_DataReceived;
           
        }

        private void nuevo_label_Click(object sender, EventArgs e)
        {
            // estos son los metodos del label en este caso ninguno
        }

        private void serialPort1_DataReceived(object sender, System.IO.Ports.SerialDataReceivedEventArgs e)
        {
            string linea = serialPort1.ReadLine();
            this.BeginInvoke(new LineReceivedEvents(LineReceived), linea);
        }

        private delegate void LineReceivedEvents(string linea);
        private void LineReceived(string linea)
        {
            nuevo_label.Text = linea;
        }

        private void boton_desaparecer_Click(object sender, EventArgs e)
        {
            if (nuevo_label.Visible == true)
            {
                nuevo_label.Visible = false;
            }
            else
            {
                nuevo_label.Visible = true;
            }
        }

    }
}
