import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._treeView1 = System.Windows.Forms.TreeView()
		self._button2 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(859, 44)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(158, 34)
		self._button1.TabIndex = 0
		self._button1.Text = "Select HL7 fle..."
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.OnClicked
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(28, 579)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(1087, 32)
		self._label1.TabIndex = 1
		self._label1.Text = "label1"
		# 
		# treeView1
		# 
		self._treeView1.Location = System.Drawing.Point(112, 65)
		self._treeView1.Name = "treeView1"
		self._treeView1.Size = System.Drawing.Size(513, 277)
		self._treeView1.TabIndex = 2
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(859, 107)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(158, 34)
		self._button2.TabIndex = 3
		self._button2.Text = "Analyze Message"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(1128, 612)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._treeView1)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "test"
		self.Click += self.OnClicked
		self.ResumeLayout(False)
		

	
	def OnClicked(self, sender, event):
		self._label1.Text = 'select your hl7 file'
		dialog = OpenFileDialog()
		##dialog.Filter = "HL7 text files (*.txt)|All Files (*.*)|*.* "
		dialog.Filter = "HL7 Text files (*.txt)|*.txt|All files (*.*)|*.*"
		dialog.FilterIndex = 1
		
		
		if dialog.ShowDialog(self) == DialogResult.OK:
			f = open(dialog.FileName)
			self._label1.Text = 'i opened the file - status'
			print 'i opened the file'
			
	def ToolStrip1ItemClicked(self, sender, e):
		pass

	def Button2Click(self, sender, e):
		pass