namespace _25_Enlazar_dos_ventanas.CheckBox_y_RadioButton
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
            this.inicio = new System.Windows.Forms.Button();
            this.salir = new System.Windows.Forms.Button();
            this.titulo = new System.Windows.Forms.Label();
            this.id_label = new System.Windows.Forms.Label();
            this.contra_label = new System.Windows.Forms.Label();
            this.id_text = new System.Windows.Forms.TextBox();
            this.contra_text = new System.Windows.Forms.TextBox();
            this.SuspendLayout();
            // 
            // inicio
            // 
            this.inicio.Location = new System.Drawing.Point(53, 284);
            this.inicio.Name = "inicio";
            this.inicio.Size = new System.Drawing.Size(75, 23);
            this.inicio.TabIndex = 2;
            this.inicio.Text = "Inicio";
            this.inicio.UseVisualStyleBackColor = true;
            this.inicio.Click += new System.EventHandler(this.inicio_Click);
            // 
            // salir
            // 
            this.salir.Location = new System.Drawing.Point(187, 284);
            this.salir.Name = "salir";
            this.salir.Size = new System.Drawing.Size(75, 23);
            this.salir.TabIndex = 3;
            this.salir.Text = "Salir";
            this.salir.UseVisualStyleBackColor = true;
            this.salir.Click += new System.EventHandler(this.salir_Click);
            // 
            // titulo
            // 
            this.titulo.AutoSize = true;
            this.titulo.Font = new System.Drawing.Font("Microsoft Sans Serif", 24F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.titulo.Location = new System.Drawing.Point(92, 20);
            this.titulo.Name = "titulo";
            this.titulo.Size = new System.Drawing.Size(144, 37);
            this.titulo.TabIndex = 6;
            this.titulo.Text = "Ventana";
            // 
            // id_label
            // 
            this.id_label.AutoSize = true;
            this.id_label.Location = new System.Drawing.Point(50, 106);
            this.id_label.Name = "id_label";
            this.id_label.Size = new System.Drawing.Size(18, 13);
            this.id_label.TabIndex = 4;
            this.id_label.Text = "ID";
            // 
            // contra_label
            // 
            this.contra_label.AutoSize = true;
            this.contra_label.Location = new System.Drawing.Point(50, 200);
            this.contra_label.Name = "contra_label";
            this.contra_label.Size = new System.Drawing.Size(61, 13);
            this.contra_label.TabIndex = 5;
            this.contra_label.Text = "Contraseña";
            // 
            // id_text
            // 
            this.id_text.Location = new System.Drawing.Point(162, 103);
            this.id_text.Name = "id_text";
            this.id_text.Size = new System.Drawing.Size(100, 20);
            this.id_text.TabIndex = 0;
            this.id_text.TextChanged += new System.EventHandler(this.textBox1_TextChanged);
            // 
            // contra_text
            // 
            this.contra_text.Location = new System.Drawing.Point(162, 197);
            this.contra_text.Name = "contra_text";
            this.contra_text.PasswordChar = '*';
            this.contra_text.Size = new System.Drawing.Size(100, 20);
            this.contra_text.TabIndex = 1;
            // 
            // ventana
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.SystemColors.ActiveCaption;
            this.ClientSize = new System.Drawing.Size(344, 346);
            this.Controls.Add(this.contra_text);
            this.Controls.Add(this.id_text);
            this.Controls.Add(this.contra_label);
            this.Controls.Add(this.id_label);
            this.Controls.Add(this.titulo);
            this.Controls.Add(this.salir);
            this.Controls.Add(this.inicio);
            this.MaximizeBox = false;
            this.MaximumSize = new System.Drawing.Size(360, 385);
            this.Name = "ventana";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Form1";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button inicio;
        private System.Windows.Forms.Button salir;
        private System.Windows.Forms.Label titulo;
        private System.Windows.Forms.Label id_label;
        private System.Windows.Forms.Label contra_label;
        private System.Windows.Forms.TextBox id_text;
        private System.Windows.Forms.TextBox contra_text;
    }
}

