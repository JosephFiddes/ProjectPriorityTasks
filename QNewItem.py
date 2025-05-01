from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import *
import sys

class QNewItem(QWidget):
	def __init__(self, taskListFileName):
		super().__init__()

		self.taskListFileName = taskListFileName

		# Subwidgets
		self.itemTitleEdit = QLineEdit()
		self.itemHasDueDateEdit = QCheckBox()
		self.itemDueDateEdit = QDateTimeEdit()
		self.itemPriorityEdit = QSpinBox()
		self.itemSubmit = QPushButton("Submit")

		self.itemSubmit.clicked.connect(self.submitNewItem)

		# Define Layout
		itemLayout = QVBoxLayout()
		itemLayout.addWidget(self.itemTitleEdit)

		itemHasDueDateLayout = QHBoxLayout()
		itemHasDueDateLayout.addWidget(QLabel("has due date?"))
		itemHasDueDateLayout.addWidget(self.itemHasDueDateEdit)
		itemLayout.addLayout(itemHasDueDateLayout)

		dateAndPriorityLayout = QGridLayout()
		dateAndPriorityLayout.addWidget(QLabel("due date:"), 0, 0)
		dateAndPriorityLayout.addWidget(self.itemDueDateEdit, 0, 1)
		dateAndPriorityLayout.addWidget(QLabel("priority:"), 1, 0)
		dateAndPriorityLayout.addWidget(self.itemPriorityEdit, 1, 1)
		itemLayout.addLayout(dateAndPriorityLayout)

		itemLayout.addWidget(self.itemSubmit)

		self.setLayout(itemLayout)

	def submitNewItem(self):
		print("to be implemented")