

class Animal(object):

	def __init__(self,sound,name,age,favorite_color):
		self.sound = sound
		self.name = name
		self.age = age
		self.favorite_color = favorite_color


	def eat(self,food):
		print("Yummy!! " + self.name + " is eating " + food )

	def description(self):
		print(self.name + " is " + self.age + " years old and loves the color " + self.favorite_color)

	def make_sound(self):
		print(self.sound *3)



cat = Animal("Meow","Lucy", "8", "purple")

cat.name = "Lucy"
cat.sound = "Meow"
cat.age = "8"
cat.favorite_color = "purple"
food = "tuna"

cat.eat(food)
cat.description()
cat.make_sound()







