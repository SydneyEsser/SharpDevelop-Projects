import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.PaleVioletRed
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.MediumVioletRed
		self._button1.Location = System.Drawing.Point(2, 252)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(113, 44)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.PaleVioletRed
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.MediumVioletRed
		self._button2.Location = System.Drawing.Point(118, 252)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(112, 44)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.PaleVioletRed
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.Color.MediumVioletRed
		self._button3.Location = System.Drawing.Point(236, 252)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(111, 44)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.LightPink
		self._label1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.MediumVioletRed
		self._label1.Location = System.Drawing.Point(2, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(345, 104)
		self._label1.TabIndex = 3
		self._label1.Text = "Sum"
		self._label1.Click += self.Label1Click
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.LightPink
		self._label3.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ForeColor = System.Drawing.Color.MediumVioletRed
		self._label3.Location = System.Drawing.Point(2, 193)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(111, 56)
		self._label3.TabIndex = 5
		self._label3.Text = "Product"
		self._label3.Click += self.Label3Click
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.LightPink
		self._label4.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.ForeColor = System.Drawing.Color.MediumVioletRed
		self._label4.Location = System.Drawing.Point(118, 127)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(111, 56)
		self._label4.TabIndex = 7
		self._label4.Text = "Average"
		self._label4.Click += self.Label4Click
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.LightPink
		self._label2.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.Color.MediumVioletRed
		self._label2.Location = System.Drawing.Point(2, 127)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(111, 56)
		self._label2.TabIndex = 8
		self._label2.Text = "Difference"
		self._label2.Click += self.Label2Click
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.LightPink
		self._label5.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.ForeColor = System.Drawing.Color.MediumVioletRed
		self._label5.Location = System.Drawing.Point(119, 193)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(111, 56)
		self._label5.TabIndex = 9
		self._label5.Text = "Absolute Value"
		self._label5.Click += self.Label5Click
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.LightPink
		self._label6.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.ForeColor = System.Drawing.Color.MediumVioletRed
		self._label6.Location = System.Drawing.Point(236, 127)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(111, 56)
		self._label6.TabIndex = 10
		self._label6.Text = "Maximum"
		self._label6.Click += self.Label6Click
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.LightPink
		self._label7.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.ForeColor = System.Drawing.Color.MediumVioletRed
		self._label7.Location = System.Drawing.Point(236, 193)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(111, 56)
		self._label7.TabIndex = 11
		self._label7.Text = "Minimum"
		self._label7.Click += self.Label7Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Crimson
		self.ClientSize = System.Drawing.Size(354, 308)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Lang88a"
		self.ResumeLayout(False)

	def Button3Click(self, sender, e):
		Application_Exit()

	def Label6Click(self, sender, e):
		pass

	def Button2Click(self, sender, e):
		self._label1.Text = ""
		self._label2.Text = ""
		self._label3.Text = ""
		self._label4.Text = ""
		self._label5.Text = ""
		self._label6.Text = ""
		self._label7.Text = ""

	def Button1Click(self, sender, e):
		self._label1.Text = "33"
		self._label2.Text = "-7"
		self._label3.Text = "260"
		self._label4.Text = "16.5"
		self._label5.Text = "7"
		self._label6.Text = "20"
		self._label7.Text = "13"

	def Label1Click(self, sender, e):
		pass

	def Label2Click(self, sender, e):
		pass

	def Label3Click(self, sender, e):
		pass

	def Label4Click(self, sender, e):
		pass

	def Label5Click(self, sender, e):
		pass

	def Label7Click(self, sender, e):
		pass