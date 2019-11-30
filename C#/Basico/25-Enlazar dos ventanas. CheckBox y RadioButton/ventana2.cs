using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace _25_Enlazar_dos_ventanas.CheckBox_y_RadioButton
{
    public partial class ventana2 : Form
    {
        public ventana2()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int x = 0;
            string selecion;
            if (checkBox1.Checked == true )
            {
                x = x + 1;
            }
            if (checkBox2.Checked == true)
            {
                x = x + 1;
            }
            if (radioButton1.Checked == true)
            {
                selecion = "credito";
            }
            else
            {
                selecion = "Debito";
            }
            MessageBox.Show("Se selecionaron: "+ x + " curso y el metodo de pago es: " + selecion);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            this.Hide();
            ventana ventana_inicio = new ventana();
            ventana_inicio.Show();
        }
    }
}
