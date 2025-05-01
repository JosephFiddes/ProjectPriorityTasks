from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import *
from QNewItem import QNewItem
from taskList import TaskList
import sys

class Window(QMainWindow):
	def __init__(self, taskList):
		super().__init__()

		#self.setGeometry(300, 300, 600, 400)
		self.setWindowTitle("Priority Task Scheduler")

		# Set the central widget of the Window. Widget will expand
		# to take up all the space in the window by default.
		originLayout = QVBoxLayout()
		originLayout.addWidget(QNewItem(taskList))
		originWidget = QWidget()
		originWidget.setLayout(originLayout)
		self.setCentralWidget(originWidget)

	#def the_button_was_clicked(self):
	#	print("Clicked!")

###########################################################################

TASKLIST_FILENAME = "priorityTasks.csv"

app = QApplication(sys.argv)
taskList = TaskList(TASKLIST_FILENAME)
window = Window(taskList)
window.show()

sys.exit(app.exec_())