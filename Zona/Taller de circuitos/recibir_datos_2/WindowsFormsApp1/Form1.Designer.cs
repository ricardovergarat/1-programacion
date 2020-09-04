namespace WindowsFormsApp1
{
    partial class Form1
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
            this.components = new System.ComponentModel.Container();
            this.label_que_cambia = new System.Windows.Forms.Label();
            this.puerto_1 = new System.IO.Ports.SerialPort(this.components);
            this.SuspendLayout();
            // 
            // label_que_cambia
            // 
            this.label_que_cambia.AutoSize = true;
            this.label_que_cambia.Font = new System.Drawing.Font("Microsoft Sans Serif", 120F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label_que_cambia.Location = new System.Drawing.Point(189, 126);
            this.label_que_cambia.Name = "label_que_cambia";
            this.label_que_cambia.Size = new System.Drawing.Size(507, 181);
            this.label_que_cambia.TabIndex = 0;
            this.label_que_cambia.Text = "label1";
            // 
            // puerto_1
            // 
            this.puerto_1.PortName = "COM3";
            this.puerto_1.DataReceived += new System.IO.Ports.SerialDataReceivedEventHandler(this.serialPort1_DataReceived);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.label_que_cambia);
            this.Name = "Form1";
            this.Text = "Form1";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label_que_cambia;
        public System.IO.Ports.SerialPort puerto_1;
    }
}

