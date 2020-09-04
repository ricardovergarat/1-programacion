using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.IO.Ports; //PERMITE EL USO DE LOS PUERTOS.

namespace PWM_LED
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            serialPort1.Open();
        }


        private void timer1_Tick(object sender, EventArgs e)
        {
            string POT = serialPort1.ReadExisting(); //changing between 0-1023
            label3.Text = POT;
            int VALUE = Convert.ToInt32(POT); // convert to int for making operations.
            label5.Text = Convert.ToString(VALUE * (5 / 1023)); //shows the voltage value
                                                                //pot=1023 the voltage showed is 5, pot=0 the voltage showed is 0.
        }
    }
}