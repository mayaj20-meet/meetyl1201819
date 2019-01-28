import turtle

turtle.pensize(7)

for i in range(5):
	turtle.hideturtle()
	turtle.pencolor("green")
	turtle.forward(500)
	turtle.left(216)

turtle.showturtle()
turtle.penup()
turtle.forward(150)
turtle.pendown()
turtle.pencolor("yellow")
turtle.begin_fill()

for i in range(3):
	turtle.forward(50)
	turtle.left(90)
turtle.right(45)
turtle.forward(35,35)
turtle.left(90)
turtle.forward(35,5)
turtle.end_fill()
turtle.reset()
 turtle.insert(square)