
class Person():
   def __init__(self, name, favorite_food ,age, color):
       self.name = name
       self.favorite_food = favorite_food
       self.age = age
       self.color = color

   def define_color(self, color):
      print ("Red")

   def print_info(self):
       print("My name is " + str(self.name) + ", I'm " + str(self.age) + " years old.")
       print("My favorite food is " + str(self.favorite_food) + " and my favorite color is " + str(self.color))


a = Person("Britney", "Pizza", 16, "red")
a.print_info()

b = Person("Jake", "sushi", 15, "yellow")
b.print_info()
