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
		layout = QVBoxLayout()

		is_periodic = str(task["IS_PERIODIC"]) == "Y"

		# Title
		title_text = str(task["TITLE"])
		if is_periodic: title_text = "periodic: " + title_text 
		self.title = QLabel(title_text)
		layout.addWidget(self.title)

		# Only show due date and estimated time to complete if item has due date
		if (str(task["HAS_DUE_DATE"]) == "Y" and not is_periodic):
			# Due date
			self.dueDate = QLabel("Due: " + str(task["DATETIME_DUE"]))
			layout.addWidget(self.dueDate)

			# Estimated time to complete
			self.estHours = QLabel(str(task["ESTIMATED_HOURS"]) + " hours")
			layout.addWidget(self.estHours)

		# Priority
		if not is_periodic:
			self.priority = QLabel("Priority: " + str(task["CUR_PRIORITY"]))
			layout.addWidget(self.priority)

		buttonsLayout = QHBoxLayout()
		# Complete button (only if periodic)
		if is_periodic:
			self.completeButton = QPushButton("Complete")
			self.completeButton.clicked.connect(self.complete)
			buttonsLayout.addWidget(self.completeButton)

		# Delete button
		self.deleteButton = QPushButton("Delete")
		self.deleteButton.clicked.connect(self.delete)
		buttonsLayout.addWidget(self.deleteButton)
		layout.addLayout(buttonsLayout)

		self.setLayout(layout)

	def delete(self):
		self.window.deleteTask(self.index)

	def complete(self):
		self.delete()