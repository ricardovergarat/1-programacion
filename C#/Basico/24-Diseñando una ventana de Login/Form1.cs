using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace _24_Diseñando_una_ventana_de_Login
{
    public partial class ventana : Form
    {
        public ventana()
        {
            InitializeComponent();
        }

        private void label3_Click(object sender, EventArgs e)
        {

        }

        private void ventana_Load(object sender, EventArgs e)
        {

        }

        private void B_salir_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void B_iniciar_Click(object sender, EventArgs e)
        {
            if (text_id.Text == "abc" && text_contrasena.Text == "123")
            {
                MessageBox.Show("se iniciado sesion");
            }
            else
            {
                MessageBox.Show("algo no coincide ..... intente denuevo");
                text_id.Text = "";
                text_contrasena.Text = "";
                text_id.Focus();
            }
        }
    }
}
