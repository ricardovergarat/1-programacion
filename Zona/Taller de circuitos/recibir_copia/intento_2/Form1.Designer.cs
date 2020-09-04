namespace intento_2
{
    partial class Ventana
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
            this.boton_desaparecer = new System.Windows.Forms.Button();
            this.nuevo_label = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // boton_desaparecer
            // 
            this.boton_desaparecer.Location = new System.Drawing.Point(566, 140);
            this.boton_desaparecer.Name = "boton_desaparecer";
            this.boton_desaparecer.Size = new System.Drawing.Size(75, 23);
            this.boton_desaparecer.TabIndex = 1;
            this.boton_desaparecer.Text = "cambio";
            this.boton_desaparecer.UseVisualStyleBackColor = true;
            this.boton_desaparecer.Click += new System.EventHandler(this.boton_desaparecer_Click);
            // 
            // nuevo_label
            // 
            this.nuevo_label.AutoSize = true;
            this.nuevo_label.Location = new System.Drawing.Point(361, 233);
            this.nuevo_label.Name = "nuevo_label";
            this.nuevo_label.Size = new System.Drawing.Size(35, 13);
            this.nuevo_label.TabIndex = 2;
            this.nuevo_label.Text = "label1";
            this.nuevo_label.Click += new System.EventHandler(this.nuevo_label_Click);
            // 
            // Ventana
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.nuevo_label);
            this.Controls.Add(this.boton_desaparecer);
            this.Name = "Ventana";
            this.Text = "Form1";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion
        private System.Windows.Forms.Button boton_desaparecer;
        private System.Windows.Forms.Label nuevo_label;
    }
}

