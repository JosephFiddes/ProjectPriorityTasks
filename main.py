from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import *
from QNewItem import QNewItem
import sys
 
class Window(QMainWindow):
	def __init__(self):
		super().__init__()

		#self.setGeometry(300, 300, 600, 400)
		self.setWindowTitle("Priority Task Scheduler")

		# Set the central widget of the Window. Widget will expand
		# to take up all the space in the window by default.
		originLayout = QVBoxLayout()
		originLayout.addWidget(QNewItem())
		originWidget = QWidget()
		originWidget.setLayout(originLayout)
		self.setCentralWidget(originWidget)

	#def the_button_was_clicked(self):
	#	print("Clicked!")
 
app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec_())