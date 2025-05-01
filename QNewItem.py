from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import *
from datetime import datetime

class QNewItem(QWidget):
	def __init__(self, taskList):
		super().__init__()

		self.taskList = taskList

		# Subwidgets
		self.titleEdit = QLineEdit()
		self.hasDueDateEdit = QCheckBox()
		self.dueDateEdit = QDateTimeEdit()
		self.hoursEdit = QSpinBox()
		self.priorityEdit = QSpinBox()
		self.submitButton = QPushButton("Submit")

		self.submitButton.clicked.connect(self.submit)

		# Define Layout
		layout = QVBoxLayout()
		layout.addWidget(self.titleEdit)

		hasDueDateLayout = QHBoxLayout()
		hasDueDateLayout.addWidget(QLabel("has due date?"))
		hasDueDateLayout.addWidget(self.hasDueDateEdit)
		layout.addLayout(hasDueDateLayout)

		dateAndPriorityLayout = QGridLayout()
		dateAndPriorityLayout.addWidget(QLabel("due date:"),    0, 0)
		dateAndPriorityLayout.addWidget(self.dueDateEdit,       0, 1)
		dateAndPriorityLayout.addWidget(QLabel("hrs to take:"), 1, 0)
		dateAndPriorityLayout.addWidget(self.hoursEdit,         1, 1)
		dateAndPriorityLayout.addWidget(QLabel("priority:"),    2, 0)
		dateAndPriorityLayout.addWidget(self.priorityEdit,      2, 1)
		layout.addLayout(dateAndPriorityLayout)

		layout.addWidget(self.submitButton)

		self.setLayout(layout)

	def submit(self):
		DTFORMATSTRING_QDateTime = "yyyy-MM-dd hh:mm"
		DTFORMATSTRING_datetime = "%Y-%m-%d %H:%M"

		newTask = {
			"TITLE": [str(self.titleEdit.text())],
			"DATETIME_DUE": [str(self.dueDateEdit.dateTime()
							.toString(DTFORMATSTRING_QDateTime))],
			"ESTIMATED_HOURS": [str(self.hoursEdit.value())],
			"DATETIME_SUBMITTED": [str(datetime.now()
							.strftime(DTFORMATSTRING_datetime))], 
			"INITIAL_PRIORITY": [str(self.priorityEdit.value())] 
		}
		self.taskList.appendTask(newTask)
		self.taskList.reset()
