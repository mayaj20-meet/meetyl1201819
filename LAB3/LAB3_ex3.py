import turtle

def thing():
turtle.speed(1)
turtle.forward(250)
turtle.right(35)
turtle.forward(150)
turtle.right(90)
turtle.forward(150)
turtle.penup()
turtle.setpos(0,0)
turtle.pendown()

turtle.right(1)
for i in range(360):
	thing()