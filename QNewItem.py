from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import *
import sys

class QNewItem(QWidget):
	def __init__(self):
		super().__init__()

		itemTitleEdit = QLineEdit()
		itemHasDueDateEdit = QCheckBox()
		itemDueDateEdit = QDateTimeEdit()
		itemPriorityEdit = QSpinBox()
		itemSubmit = QPushButton("Submit")

		itemLayout = QVBoxLayout()
		itemLayout.addWidget(itemTitleEdit)

		itemHasDueDateLayout = QHBoxLayout()
		itemHasDueDateLayout.addWidget(QLabel("has due date?"))
		itemHasDueDateLayout.addWidget(itemHasDueDateEdit)
		itemLayout.addLayout(itemHasDueDateLayout)

		dateAndPriorityLayout = QGridLayout()
		dateAndPriorityLayout.addWidget(QLabel("due date:"), 0, 0)
		dateAndPriorityLayout.addWidget(itemDueDateEdit, 0, 1)
		dateAndPriorityLayout.addWidget(QLabel("priority:"), 1, 0)
		dateAndPriorityLayout.addWidget(itemPriorityEdit, 1, 1)
		itemLayout.addLayout(dateAndPriorityLayout)

		itemLayout.addWidget(itemSubmit)

		self.setLayout(itemLayout)