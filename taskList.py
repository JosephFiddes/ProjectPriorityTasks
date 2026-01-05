import pandas as pd
from datetime import datetime, timedelta
from DTFormatStrings import *

class TaskList():
	def __init__(self, filename):
		self.filename = filename

		self.readFromFile()

	def readFromFile(self):
		try:
			self.tasks = pd.read_csv(self.filename)
		except FileNotFoundError:
			print("Couldn't find " + self.filename)
			print("If " + self.filename + " exists, then the program may overwrite it.")
			print("Be sure to back up " + self.filename + " to a new location.")
			input("Press ENTER to continue.")
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

	def completeTask(self, taskIndex):
		# Each element in a task appears in an array by itself.
		# This is awkward when reading, so an additional copy is made where
		# the elements are removed from their arrays.
		taskToWrite = self.tasks.loc[[taskIndex]].to_dict(orient='list')
		taskToRead = {k: v[0] for k, v in taskToWrite.items()}

		if str(taskToRead["IS_PERIODIC"]) != "Y": 
			self.deleteTask(taskIndex)
			return

		# Find the new due date/time for the task
		periodDays = int(taskToRead["PERIOD"])
		periodDeltaTime = timedelta(days=periodDays)

		resetBehaviour = str(taskToRead["RESET"])
		onCompleteOption = "on completion"
		atEndOfPeriodOption = "strictly periodic"
		if resetBehaviour == atEndOfPeriodOption:
			oldDueDateTime = datetime.strptime(taskToRead["DATETIME_DUE"], 
				DTFORMATSTRING_datetime)
		else:
			oldDueDateTime = datetime.now()
			if resetBehaviour != onCompleteOption:
				print("Warning: unexpected value in RESET (task " + taskIndex + ")")

		newDueDateTime = oldDueDateTime + periodDeltaTime
		taskToWrite["DATETIME_DUE"] = [str(newDueDateTime
				.strftime(DTFORMATSTRING_datetime))]

		# Remove old task and add new task
		self.deleteTask(taskIndex)
		self.appendTask(taskToWrite)
		

	def isDue(self, task):
		dueDateTime = datetime.strptime(task["DATETIME_DUE"], 
			DTFORMATSTRING_datetime)
		now = datetime.now()
		return (dueDateTime - now).days < 0

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