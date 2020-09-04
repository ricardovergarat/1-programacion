using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
// esta biblioteca sirve para conectar con los puertos del arduino
using System.IO.Ports;

namespace WindowsFormsApp1
{
    public partial class Form1 : Form
    {
        private SerialPort mi_entrada;
        public Form1()
        {
            InitializeComponent();
            mi_entrada = new SerialPort();
            mi_entrada.PortName = "COM3";
            mi_entrada.BaudRate = 9600;
            mi_entrada.DtrEnable = true;
            mi_entrada.Open();
            mi_entrada.DataReceived = mi_entrada.DataReceived * 10;

        }
        
        private void resivir_datos(object sender, System.IO.Ports.SerialDataReceivedEventsArgs e)
        {
            string dato = mi_entrada.ReadLine();
        }

        private void serialPort1_DataReceived(object sender, SerialDataReceivedEventArgs e)
        {
            string dato = mi_entrada.ReadLine();
        }
    }
}
