namespace _23_Propiedades_de_una_Ventana
{
    partial class ventana
    {
        /// <summary>
        /// Variable del diseñador necesaria.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Limpiar los recursos que se estén usando.
        /// </summary>
        /// <param name="disposing">true si los recursos administrados se deben desechar; false en caso contrario.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Código generado por el Diseñador de Windows Forms

        /// <summary>
        /// Método necesario para admitir el Diseñador. No se puede modificar
        /// el contenido de este método con el editor de código.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(ventana));
            this.B = new System.Windows.Forms.Button();
            this.cuadro_texto = new System.Windows.Forms.TextBox();
            this.SuspendLayout();
            // 
            // B
            // 
            this.B.BackColor = System.Drawing.SystemColors.Window;
            this.B.Location = new System.Drawing.Point(514, 301);
            this.B.Name = "B";
            this.B.Size = new System.Drawing.Size(75, 23);
            this.B.TabIndex = 0;
            this.B.Text = "BBB";
            this.B.UseVisualStyleBackColor = false;
            this.B.Click += new System.EventHandler(this.button1_Click);
            // 
            // cuadro_texto
            // 
            this.cuadro_texto.BackColor = System.Drawing.SystemColors.InactiveCaption;
            this.cuadro_texto.Location = new System.Drawing.Point(180, 111);
            this.cuadro_texto.Name = "cuadro_texto";
            this.cuadro_texto.Size = new System.Drawing.Size(100, 20);
            this.cuadro_texto.TabIndex = 1;
            this.cuadro_texto.TextChanged += new System.EventHandler(this.textBox1_TextChanged);
            // 
            // ventana
            // 
            this.AcceptButton = this.B;
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.SystemColors.Highlight;
            this.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("$this.BackgroundImage")));
            this.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.ClientSize = new System.Drawing.Size(948, 581);
            this.Controls.Add(this.cuadro_texto);
            this.Controls.Add(this.B);
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.Name = "ventana";
            this.Text = "Dale vergo";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button B;
        private System.Windows.Forms.TextBox cuadro_texto;
    }
}

