class Cat():
	def __init__(self, name, age):
		self.name = name
		self.age = age 

	def birthday(self):
		print(str(self.name) + " is having its " + str(self.age) +"th birthday!")
		

my_cat = Cat("Salem", 8)
my_cat.birthday()