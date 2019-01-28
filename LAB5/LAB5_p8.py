
class Cake():
	def __init__(self, cake_flavor):
		self.cake_flavor = cake_flavor

	def eat(self):
		print("Yummy!!! Eating a " + self.cake_flavor + " cake :)")

cake = Cake("chocolate")
cake.eat()
# what I want to be printed: Yummy!!! Eating a chocolate cake :)
