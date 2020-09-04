namespace Monitor_signos_vitales
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
            System.Windows.Forms.DataVisualization.Charting.ChartArea chartArea1 = new System.Windows.Forms.DataVisualization.Charting.ChartArea();
            System.Windows.Forms.DataVisualization.Charting.Legend legend1 = new System.Windows.Forms.DataVisualization.Charting.Legend();
            System.Windows.Forms.DataVisualization.Charting.Series series1 = new System.Windows.Forms.DataVisualization.Charting.Series();
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Ventana));
            this.texto_temperatura = new System.Windows.Forms.Label();
            this.texto_punto_grados = new System.Windows.Forms.Label();
            this.chart1 = new System.Windows.Forms.DataVisualization.Charting.Chart();
            this.texto_respiraciones = new System.Windows.Forms.Label();
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            ((System.ComponentModel.ISupportInitialize)(this.chart1)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            this.SuspendLayout();
            // 
            // texto_temperatura
            // 
            this.texto_temperatura.AutoSize = true;
            this.texto_temperatura.Cursor = System.Windows.Forms.Cursors.Default;
            this.texto_temperatura.Font = new System.Drawing.Font("Microsoft Sans Serif", 120F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.texto_temperatura.ForeColor = System.Drawing.SystemColors.ActiveCaption;
            this.texto_temperatura.Location = new System.Drawing.Point(12, 269);
            this.texto_temperatura.Name = "texto_temperatura";
            this.texto_temperatura.Size = new System.Drawing.Size(255, 181);
            this.texto_temperatura.TabIndex = 1;
            this.texto_temperatura.Text = "38";
            this.texto_temperatura.Click += new System.EventHandler(this.label1_Click);
            // 
            // texto_punto_grados
            // 
            this.texto_punto_grados.AutoSize = true;
            this.texto_punto_grados.Font = new System.Drawing.Font("Microsoft Sans Serif", 120F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.texto_punto_grados.ForeColor = System.Drawing.SystemColors.ActiveCaption;
            this.texto_punto_grados.Location = new System.Drawing.Point(218, 242);
            this.texto_punto_grados.Name = "texto_punto_grados";
            this.texto_punto_grados.Size = new System.Drawing.Size(141, 181);
            this.texto_punto_grados.TabIndex = 2;
            this.texto_punto_grados.Text = "°";
            this.texto_punto_grados.Click += new System.EventHandler(this.texto_punto_grados_Click);
            // 
            // chart1
            // 
            chartArea1.Name = "ChartArea1";
            this.chart1.ChartAreas.Add(chartArea1);
            legend1.Name = "Legend1";
            this.chart1.Legends.Add(legend1);
            this.chart1.Location = new System.Drawing.Point(443, 150);
            this.chart1.Name = "chart1";
            this.chart1.Palette = System.Windows.Forms.DataVisualization.Charting.ChartColorPalette.SeaGreen;
            series1.ChartArea = "ChartArea1";
            series1.Legend = "Legend1";
            series1.Name = "Series1";
            this.chart1.Series.Add(series1);
            this.chart1.Size = new System.Drawing.Size(300, 300);
            this.chart1.TabIndex = 4;
            this.chart1.Text = "chart2";
            this.chart1.Click += new System.EventHandler(this.chart1_Click);
            // 
            // texto_respiraciones
            // 
            this.texto_respiraciones.AutoSize = true;
            this.texto_respiraciones.BackColor = System.Drawing.SystemColors.ControlLightLight;
            this.texto_respiraciones.Font = new System.Drawing.Font("Microsoft Sans Serif", 36F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.texto_respiraciones.Location = new System.Drawing.Point(941, 325);
            this.texto_respiraciones.Name = "texto_respiraciones";
            this.texto_respiraciones.Size = new System.Drawing.Size(78, 55);
            this.texto_respiraciones.TabIndex = 5;
            this.texto_respiraciones.Text = "40";
            this.texto_respiraciones.Click += new System.EventHandler(this.texto_respiraciones_Click);
            // 
            // pictureBox1
            // 
            this.pictureBox1.Image = global::Monitor_signos_vitales.Properties.Resources._21;
            this.pictureBox1.Location = new System.Drawing.Point(812, 163);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(350, 341);
            this.pictureBox1.TabIndex = 3;
            this.pictureBox1.TabStop = false;
            // 
            // Ventana
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.SystemColors.Highlight;
            this.ClientSize = new System.Drawing.Size(1306, 752);
            this.Controls.Add(this.texto_respiraciones);
            this.Controls.Add(this.chart1);
            this.Controls.Add(this.pictureBox1);
            this.Controls.Add(this.texto_punto_grados);
            this.Controls.Add(this.texto_temperatura);
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.MaximumSize = new System.Drawing.Size(1920, 1080);
            this.MinimumSize = new System.Drawing.Size(535, 351);
            this.Name = "Ventana";
            this.Text = "Sensor signos vitales betha";
            ((System.ComponentModel.ISupportInitialize)(this.chart1)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label texto_temperatura;
        private System.Windows.Forms.Label texto_punto_grados;
        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.DataVisualization.Charting.Chart chart1;
        private System.Windows.Forms.Label texto_respiraciones;
    }
}

