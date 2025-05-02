from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import *
from QNewItem import QNewItem
from QExistingItem import QExistingItem
from taskList import TaskList
import sys

class Window(QMainWindow):
	def __init__(self, taskList):
		super().__init__()

		self.taskList = taskList

		#self.setGeometry(300, 300, 600, 400)
		self.setWindowTitle("Priority Task Scheduler")

		# Set the central widget of the Window. Widget will expand
		# to take up all the space in the window by default.
		self.originLayout = QVBoxLayout()
		self.originLayout.addWidget(QNewItem(self))
		originWidget = QWidget()
		originWidget.setLayout(self.originLayout)
		self.setCentralWidget(originWidget)

		self.existingTasksLayout = QVBoxLayout()
		self.originLayout.addLayout(self.existingTasksLayout)
		self.refreshTasks()

	def refreshTasks(self):
		self.taskList.reset()

		self.removeWidgetsFromLayout(self.existingTasksLayout)

		for index, task in taskList.tasks.iterrows():
			self.existingTasksLayout.addWidget(
				QExistingItem(self, index, task))

	# Credit Blaa_Thor on stack exchange
	# https://stackoverflow.com/a/25330164
	@staticmethod
	def removeWidgetsFromLayout(layout):
		for i in reversed(range(layout.count())): 
			widgetToRemove = layout.itemAt(i).widget()
			# remove it from the layout list
			layout.removeWidget(widgetToRemove)
			# remove it from the gui
			widgetToRemove.setParent(None)

	def submitTask(self, task):
		self.taskList.appendTask(task)
		self.refreshTasks()

	def deleteTask(self, taskIndex):
		self.taskList.deleteTask(taskIndex)
		self.refreshTasks()

###########################################################################

TASKLIST_FILENAME = "priorityTasks.csv"

app = QApplication(sys.argv)
taskList = TaskList(TASKLIST_FILENAME)
window = Window(taskList)
window.show()

sys.exit(app.exec_())