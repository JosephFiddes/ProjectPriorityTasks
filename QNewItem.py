from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import *
from datetime import datetime

class QNewItem(QWidget):
	def __init__(self, window):
		super().__init__()

		# Reference to window that new item interface exists upon.
		# Note: I don't really love this, as the two objects are coupled
		# in a not super object-oriented hierarchical way, but it be
		# like that sometimes
		self.window = window

		# Subwidgets
		self.titleEdit = QLineEdit()
		self.hasDueDateEdit = QCheckBox()
		self.dueDateEdit = QDateTimeEdit()
		self.hoursEdit = QSpinBox()
		self.priorityEdit = QSpinBox()
		self.submitButton = QPushButton("Submit")
		self.refreshButton = QPushButton("Refresh")

		self.submitButton.clicked.connect(self.submit)
		self.refreshButton.clicked.connect(self.refresh)

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
		layout.addWidget(self.refreshButton)

		self.setLayout(layout)

	def submit(self):
		DTFORMATSTRING_QDateTime = "yyyy-MM-dd hh:mm"
		DTFORMATSTRING_datetime = "%Y-%m-%d %H:%M"

		hasDueDate = "N"
		if self.hasDueDateEdit.isChecked():
			hasDueDate = "Y"

		priority = str(self.priorityEdit.value())
		newTask = {
			"TITLE": [str(self.titleEdit.text())],
			"HAS_DUE_DATE": [hasDueDate],
			"DATETIME_DUE": [str(self.dueDateEdit.dateTime()
							.toString(DTFORMATSTRING_QDateTime))],
			"ESTIMATED_HOURS": [str(self.hoursEdit.value())],
			"DATETIME_SUBMITTED": [str(datetime.now()
							.strftime(DTFORMATSTRING_datetime))], 
			"INITIAL_PRIORITY": [priority],
			"CUR_PRIORITY": [priority] 
		}

		self.window.submitTask(newTask)

	def refresh(self):
		self.window.refreshTasks()