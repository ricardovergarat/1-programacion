namespace _24_Diseñando_una_ventana_de_Login
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
            this.B_iniciar = new System.Windows.Forms.Button();
            this.B_salir = new System.Windows.Forms.Button();
            this.text_id = new System.Windows.Forms.TextBox();
            this.ID_label = new System.Windows.Forms.Label();
            this.contrasena_Label = new System.Windows.Forms.Label();
            this.Titulo = new System.Windows.Forms.Label();
            this.text_contrasena = new System.Windows.Forms.TextBox();
            this.SuspendLayout();
            // 
            // B_iniciar
            // 
            this.B_iniciar.Location = new System.Drawing.Point(65, 278);
            this.B_iniciar.Name = "B_iniciar";
            this.B_iniciar.Size = new System.Drawing.Size(75, 23);
            this.B_iniciar.TabIndex = 2;
            this.B_iniciar.Text = "Iniciar";
            this.B_iniciar.UseVisualStyleBackColor = true;
            this.B_iniciar.Click += new System.EventHandler(this.B_iniciar_Click);
            // 
            // B_salir
            // 
            this.B_salir.Location = new System.Drawing.Point(235, 278);
            this.B_salir.Name = "B_salir";
            this.B_salir.Size = new System.Drawing.Size(75, 23);
            this.B_salir.TabIndex = 3;
            this.B_salir.Text = "Salir";
            this.B_salir.UseVisualStyleBackColor = true;
            this.B_salir.Click += new System.EventHandler(this.B_salir_Click);
            // 
            // text_id
            // 
            this.text_id.Location = new System.Drawing.Point(221, 87);
            this.text_id.Name = "text_id";
            this.text_id.Size = new System.Drawing.Size(100, 20);
            this.text_id.TabIndex = 0;
            // 
            // ID_label
            // 
            this.ID_label.AutoSize = true;
            this.ID_label.Location = new System.Drawing.Point(79, 90);
            this.ID_label.Name = "ID_label";
            this.ID_label.Size = new System.Drawing.Size(18, 13);
            this.ID_label.TabIndex = 3;
            this.ID_label.Text = "ID";
            // 
            // contrasena_Label
            // 
            this.contrasena_Label.AutoSize = true;
            this.contrasena_Label.Location = new System.Drawing.Point(79, 198);
            this.contrasena_Label.Name = "contrasena_Label";
            this.contrasena_Label.Size = new System.Drawing.Size(61, 13);
            this.contrasena_Label.TabIndex = 4;
            this.contrasena_Label.Text = "Contraseña";
            // 
            // Titulo
            // 
            this.Titulo.AutoSize = true;
            this.Titulo.Font = new System.Drawing.Font("Arial", 15.75F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.Titulo.Location = new System.Drawing.Point(101, 26);
            this.Titulo.Name = "Titulo";
            this.Titulo.Size = new System.Drawing.Size(177, 24);
            this.Titulo.TabIndex = 5;
            this.Titulo.Text = "Ventana de login";
            this.Titulo.Click += new System.EventHandler(this.label3_Click);
            // 
            // text_contrasena
            // 
            this.text_contrasena.Location = new System.Drawing.Point(221, 195);
            this.text_contrasena.Name = "text_contrasena";
            this.text_contrasena.PasswordChar = '-';
            this.text_contrasena.Size = new System.Drawing.Size(100, 20);
            this.text_contrasena.TabIndex = 1;
            // 
            // ventana
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.SystemColors.Highlight;
            this.ClientSize = new System.Drawing.Size(383, 336);
            this.Controls.Add(this.text_contrasena);
            this.Controls.Add(this.Titulo);
            this.Controls.Add(this.contrasena_Label);
            this.Controls.Add(this.ID_label);
            this.Controls.Add(this.text_id);
            this.Controls.Add(this.B_salir);
            this.Controls.Add(this.B_iniciar);
            this.Cursor = System.Windows.Forms.Cursors.Arrow;
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.MaximizeBox = false;
            this.MaximumSize = new System.Drawing.Size(399, 375);
            this.Name = "ventana";
            this.Text = "Login";
            this.Load += new System.EventHandler(this.ventana_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button B_iniciar;
        private System.Windows.Forms.Button B_salir;
        private System.Windows.Forms.TextBox text_id;
        private System.Windows.Forms.Label ID_label;
        private System.Windows.Forms.Label contrasena_Label;
        private System.Windows.Forms.Label Titulo;
        private System.Windows.Forms.TextBox text_contrasena;
    }
}

