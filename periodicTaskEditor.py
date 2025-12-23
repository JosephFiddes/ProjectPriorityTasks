from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import *
from datetime import datetime
from DTFormatStrings import *

class PeriodicTaskEditor(QMainWindow):
	onCompleteOption = "on completion"
	atEndOfPeriodOption = "strictly periodic"

	def __init__(self, parentWindow):
		super().__init__(parentWindow)

		#self.setGeometry(300, 300, 600, 400)
		self.setWindowTitle("Periodic Task Editor")

		# Set the central widget of the Window. Widget will expand
		# to take up all the space in the window by default.
		self.originLayout = QVBoxLayout()
		originWidget = QWidget()
		originWidget.setLayout(self.originLayout)
		self.setCentralWidget(originWidget)

		# Subwidgets
		layout = QVBoxLayout()
		self.titleEdit = QLineEdit()
		layout.addWidget(self.titleEdit)

		# Start Now?
		startNowLayout = QHBoxLayout()
		startNowLayout.addWidget(QLabel("start now?"))
		self.startNowEdit = QCheckBox()
		startNowLayout.addWidget(self.startNowEdit)
		layout.addLayout(startNowLayout)

		# or else start on (some date/time)
		dueDateLayout = QHBoxLayout()
		dueDateLayout.addWidget(QLabel("or else start on:"))
		self.dueDateEdit = QDateTimeEdit()
		dueDateLayout.addWidget(self.dueDateEdit)
		layout.addLayout(dueDateLayout)

		# Period (days)
		periodLayout = QHBoxLayout()
		periodLayout.addWidget(QLabel("period (days):"))
		self.periodEdit = QSpinBox()
		periodLayout.addWidget(self.periodEdit)
		layout.addLayout(periodLayout)	

		# When to reset? (on completion of task or at end of period)
		resetLayout = QHBoxLayout()
		resetLayout.addWidget(QLabel("reset:"))
		self.resetEdit = QComboBox()
		self.resetEdit.addItem(PeriodicTaskEditor.onCompleteOption)
		self.resetEdit.addItem(PeriodicTaskEditor.atEndOfPeriodOption)
		resetLayout.addWidget(self.resetEdit)
		layout.addLayout(resetLayout)

		# Submit
		self.submitButton = QPushButton("Submit")
		self.submitButton.clicked.connect(self.submit)
		layout.addWidget(self.submitButton)

		self.originLayout.addLayout(layout)

	def submit(self):

		now = datetime.now()

		if self.startNowEdit.isChecked():
			dueDateTimeStr = str(now
				.strftime(DTFORMATSTRING_datetime))
		else:
			dueDateTimeStr = str(self.dueDateEdit.dateTime()
				.toString(DTFORMATSTRING_QDateTime))

		nowStr = str(now.strftime(DTFORMATSTRING_datetime))

		priority = str(float('inf'))

		period = str(max(1, self.periodEdit.value()))
		resetOn = str(self.resetEdit.currentText())

		newTask = {
			"TITLE": [str(self.titleEdit.text())],
			"IS_PERIODIC": ["Y"],
			"HAS_DUE_DATE": ["Y"],
			"DATETIME_DUE": [dueDateTimeStr],
			"ESTIMATED_HOURS": [str(0)],
			"DATETIME_SUBMITTED": [nowStr], 
			"INITIAL_PRIORITY": [priority],
			"CUR_PRIORITY": [priority],
			"PERIOD": [period],
			"RESET": [resetOn]
		}

		self.parent().submitTask(newTask)

		self.close()