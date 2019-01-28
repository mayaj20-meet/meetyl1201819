

class Person(object):

	def __init__(self,name,age,city,gender,haircolor):
		self.name = name
		self.age = age 
		self.city = city
		self.gender = gender
		self.haircolor = haircolor

	def eat(self,breakfast):
		print("Ayeee! " + self.name + " is having " + breakfast + " with orange juice")

	def play(self,sport):
		print("Yo! " + self.name + " is playing " + sport + " at the moment.")

X = Person("Johnie", "17", "Boston", "Male", "brown")

X.name = "Johnie"
X.age = "17"
X.city = "Boston"
X.gender = "Male"
X.haircolor = "brown"
breakfast = "pancakes"
sport = "volleyball"
X.eat(breakfast)
X.play(sport)

