import pandas as pd

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
		print(self.tasks)

	def appendTask(self, task):
		self.tasks = pd.concat([self.tasks, pd.DataFrame(task)], 
			ignore_index=True)

	def deleteTask(self, taskIndex):
		print(taskIndex)
		self.tasks.drop([taskIndex], axis='index', inplace=True)