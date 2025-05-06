import pandas as pd
from datetime import datetime, timedelta

class TaskList():
	def __init__(self, filename):
		self.filename = filename

		self.readFromFile()

	def readFromFile(self):
		try:
			self.tasks = pd.read_csv(self.filename)
		except FileNotFoundError:
			self.tasks = pd.DataFrame(columns=["TITLE"])

	def writeToFile(self):
		self.tasks.to_csv(self.filename, index=False)

	def reset(self):
		print(self.tasks)
		self.writeToFile()
		self.readFromFile()
		self.sort()
		print(self.tasks)

	def appendTask(self, task):
		self.tasks = pd.concat([self.tasks, pd.DataFrame(task)], 
			ignore_index=True)

	def deleteTask(self, taskIndex):
		self.tasks.drop([taskIndex], axis='index', inplace=True)

	def sort(self):
		now = datetime.now()
		self.tasks["CUR_PRIORITY"] = self.tasks.apply(
			lambda task : self.calculatePriority(task, now), 
			axis=1)

		self.tasks.sort_values(by="CUR_PRIORITY", ascending=False, inplace=True)

	@staticmethod
	def calculatePriority(task, now):
		if "HAS_DUE_DATE" not in task.keys() or task["HAS_DUE_DATE"] != "Y":
			return task["INITIAL_PRIORITY"]

		# Get required datetimes and deltas in the correct format		
		DTFORMATSTRING_datetime = "%Y-%m-%d %H:%M"
		dueDateTime = datetime.strptime(task["DATETIME_DUE"], 
			DTFORMATSTRING_datetime)
		submittedDateTime = datetime.strptime(task["DATETIME_SUBMITTED"], 
			DTFORMATSTRING_datetime)
		durationDelta = timedelta(hours=task["ESTIMATED_HOURS"])

		# start due = Get due date - est time
		dueStartDateTime = dueDateTime - durationDelta
		# time to go = start due - cur date
		timeRemainingDelta = dueStartDateTime - now
		# total time = initial due - start due
		totalDelta = dueStartDateTime - submittedDateTime

		timeRemaining = max(timeRemainingDelta.total_seconds(), 0.0)
		totalTime = max(totalDelta.total_seconds(), 0.0)

		# Priority increases as time remaining decreases.
		# 1/x time remaining => x times priority
		epsilon = 0.1
		if timeRemaining > epsilon:
			priority = task["INITIAL_PRIORITY"] * totalTime / timeRemaining
		else:
			priority = float('inf')
		return priority