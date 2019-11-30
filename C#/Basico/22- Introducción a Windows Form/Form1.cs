using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace _22__Introducción_a_Windows_Form
{
    public partial class Form1 : Form
    {
        public Form1() // este es el metodo contructor
        {
            InitializeComponent(); // va a llamar a este metodo
        }

        private void button1_Click(object sender, EventArgs e) //EventArgs e ------> esto guarda un evento
        {
            this.Close(); // los metodos son acciones
        }
    }
}
