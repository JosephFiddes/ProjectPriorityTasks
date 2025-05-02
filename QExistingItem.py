from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import *

class QExistingItem(QWidget):
	def __init__(self, window, index, task):
		super().__init__()

		# Reference to window that new item interface exists upon.
		# Note: I don't really love this, as the two objects are coupled
		# in a not super object-oriented hierarchical way, but it be
		# like that sometimes
		self.window = window
		self.index = index

		# Subwidgets
		self.title = QLabel(str(task["TITLE"]))
		self.dueDate = QLabel("Due: " + str(task["DATETIME_DUE"]))
		self.estHours = QLabel(str(task["ESTIMATED_HOURS"]) + " hours")
		self.priority = QLabel("Priority: " + str(task["INITIAL_PRIORITY"]))
		self.deleteButton = QPushButton("Delete")

		self.deleteButton.clicked.connect(self.delete)

		# Define Layout
		layout = QVBoxLayout()
		layout.addWidget(self.title)
		layout.addWidget(self.dueDate)
		layout.addWidget(self.estHours)
		layout.addWidget(self.priority)
		layout.addWidget(self.deleteButton)

		self.setLayout(layout)

	def delete(self):
		self.window.deleteTask(self.index)