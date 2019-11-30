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
    public partial class ventana : Form
    {
        public ventana()
        {
            InitializeComponent();
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void inicio_Click(object sender, EventArgs e)
        {
            if (id_text.Text == "abc" && contra_text.Text == "123")
            {
                this.Hide(); // esto oculta la ventana
                ventana2 nueeva_ventana = new ventana2();
                nueeva_ventana.Show();
            }
            else
            {
                MessageBox.Show("algo no coincide ..... intente denuevo");
                id_text.Text = "";
                contra_text.Text = "";
                id_text.Focus();
            }
        }

        private void salir_Click(object sender, EventArgs e)
        {
            this.Close();
        }
    }
}
