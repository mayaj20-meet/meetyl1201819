class Bear():
	def __init__(self, name):
		self.name = name

	def say_hi(self):
		print("Hi! I’m a bear. My name is " + self.name)

	def new_bear(self):
		print("A new bear created. Its name is: " + self.name)
	
	
my_bear = Bear("Danny")
new_bear = Bear ("Johnie")
my_bear.say_hi()
my_bear.new_bear()
