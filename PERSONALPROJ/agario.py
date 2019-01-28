###################################################################################

## GETTING STARTED

 # S1:
from personal_project import Ball
import time
import turtle
from turtle import *
import random
import math
import sys
import pygame
colormode(255)
bgpic("smile.gif")
tracer(0)
hideturtle()
turtle.penup()
turtle.goto(-500,250)
score = 0
running = True
sleep = 0.0077
screen_width = turtle.getcanvas().winfo_width()//2
screen_height =turtle.getcanvas().winfo_height()//2

pygame.mixer.init()
pygame.mixer.music.load("Countdown.wav") 
pygame.mixer.music.play(0)

###################################################################################

## PART 0: CREATING THE BALLS

## 0.1:
my_ball = Ball(0,-10,5,5,25,"red") ## <=== The ball that we actually control

## 0.2:

number_of_balls = 10
minimum_ball_radius = 5
maximum_ball_radius = 80
minimum_ball_dx = -2
maximum_ball_dx = 2
minimum_ball_dy = -2
maximum_ball_dy = 2

## 0.3:
balls = []

## 0.4:
for i in range (number_of_balls):

# 0.4 a):
	x = random.randint (int (-screen_width) + int (maximum_ball_radius) , int (screen_width) - int (maximum_ball_radius)) # <=== i
	y = random.randint (int (-screen_height) + int (maximum_ball_radius), int (screen_height) - int (maximum_ball_radius)) # <=== ii
	dx = random.randint (minimum_ball_dx,maximum_ball_dx)  # <=== iii
	dy = random.randint (minimum_ball_dy,maximum_ball_dy)  # <=== iv
	radius = random.randint (minimum_ball_radius,maximum_ball_radius) # <=== v
	color = (random.random(), random.random(), random.random()) # <=== vi


	if dx == 0:
		dx = random.randint(minimum_ball_dx,maximum_ball_dx)
		dy = random.randint(minimum_ball_dy,maximum_ball_dy)

	if dy == 0:
		dy = random.randint(minimum_ball_dy,maximum_ball_dy)


	ball1 = Ball(x, y, dx, dy, radius, color)

# 0.4 c):
	balls.append (ball1)


###################################################################################

## PART 1: MOVE ALL BALLS 

# 1.1:
def move_all_balls():  ## <=== This ensures that all balls move

# 1.2:
	for z in balls:
		z.move(screen_width, screen_height)

###################################################################################

## PART 2: CHECK FOR BALL COLLISIONS

# 2.1:
def collide(ball_a, ball_b):
	ball_a_pos = ball_a.pos()
	ball_b_pos = ball_b.pos()

# 2.2:
	if ball_a == ball_b :
		return False
		
	ball_a.xcor()	
	ball_a.ycor()	
	ball_b.xcor()	
	ball_b.ycor()	

# 2.3:
	distance_between_centers = ((ball_a.xcor()-ball_b.xcor())**2 + (ball_a.ycor()-ball_b.ycor())**2)**0.5

# 2.4:

	if distance_between_centers+10 <= ball_a.radius + ball_b.radius:
		score =+ 1
		return True

###################################################################################

## PART 3 : CHECK COLLISION FOR ALL BALLS

# 3.1

def check_all_balls_collision():
	global running
	global score


# 3.2:
	for ball_a in BALLS:

		for ball_b in BALLS:

			if collide(ball_a,ball_b) == True:

				score =+1
				radius_a = ball_a.radius
				radius_b = ball_b.radius

				X_coordinate = random.randint(int(-screen_width) + int(maximum_ball_radius) , int(screen_width) - int(maximum_ball_radius))
				Y_coordinate = random.randint(int(-screen_height) + int(maximum_ball_radius),int(screen_height) - int(maximum_ball_radius))
				X_axis_speed = random.randint(minimum_ball_dx,maximum_ball_dx)


				while X_axis_speed == 0:
					 X_axis_speed = random.randint(minimum_ball_dx,maximum_ball_dx)
				Y_axis_speed  = random.randint(minimum_ball_dy,maximum_ball_dy)

				while Y_axis_speed  == 0:
					Y_axis_speed  = random.randint(minimum_ball_dy,maximum_ball_dy)
				radius = random.randint(minimum_ball_radius, maximum_ball_radius)

				color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
				ball_a.color(color)

				if ball_a < ball_b:
					ball_a.goto(X_coordinate, Y_coordinate) 
					ball_a.dx = X_axis_speed 

	
					ball_a.dy = Y_axis_speed
					ball_a.shapesize(radius/10)
					ball_a.color = color
					ball_a.radius += 10
					score += 1
					ball_a.shapesize(ball_a.radius/10)
					ball_a.radius += 10
					ball_b.shapesize(ball_b.radius/10)

# 3.4:
				else: 
					ball_b.goto(X_coordinate, Y_coordinate)
					ball_b.dx = X_axis_speed 
					ball_b.dy = Y_axis_speed
					ball_b.shapesize(radius/10)
					ball_b.color = color
					ball_a.shapesize(ball_b.radius)
					ball_b.radius += 10
			
					ball_a.shapesize(ball_a.radius/10)
					ball_b.shapesize(ball_b.radius/10)


###################################################################################

## PART 4: CHECK COLLISION WITH MY BALL


# 4.1:
def check_myball_collision():
	global score
	for i in balls:
		if collide(i,my_ball) == True:
			radius_i = i.radius
			radius_my_ball = my_ball.radius

			if my_ball.radius < i.radius:
				running = False
				turtle.clear()
				goto(-560,0)
				turtle.bgpic("KA.gif")
				turtle.color("blue")
				write("YOU LOST GAME OVERRR!!", move = False, font=("Arial", 70, "bold"))
				
				time.sleep(2)
				sys.exit("why not try again?")

			else:
				X_coordinate = random.randint(int(-screen_width) + int(maximum_ball_radius) , int(screen_width) - int(maximum_ball_radius))
				Y_coordinate = random.randint(int(-screen_height) + int(maximum_ball_radius),int(screen_height) - int(maximum_ball_radius))
				X_axis_speed = random.randint(minimum_ball_dx,maximum_ball_dx)
				Y_axis_speed  = random.randint(minimum_ball_dy,maximum_ball_dy)


				while X_axis_speed == 0:
					X_axis_speed = random.randint(minimum_ball_dx,maximum_ball_dx)


				while Y_axis_speed  == 0:
					Y_axis_speed  = random.randint(minimum_ball_dy,maximum_ball_dy)

				radius = random.randint(minimum_ball_radius, maximum_ball_radius)

				score += 1
			
				i.goto(X_coordinate, Y_coordinate)
				i.dx = X_axis_speed 
				i.dy = Y_axis_speed
				i.shapesize(radius/10)
				color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
				i.color(color)
				my_ball.radius += 5
				my_ball.shapesize(my_ball.radius/10)


	return True

###################################################################################

## EXTRA: COUNT TO 3

turtle.color("black")

turtle.goto(-575,0)
turtle.write("WELCOME TO MAYAS COOL GAME!", move=False, align="left", font=("Arial", 50, "bold"))
time.sleep(2)
turtle.clear()

turtle.goto(-350,0)
turtle.write("THE GAME WILL BEGIN...", move=False, align="left", font=("Arial", 50, "bold"))
time.sleep(1)
turtle.clear()

turtle.write("ON THE COUNT OF 3", move=False, align="left", font=("Arial", 50, "bold"))
time.sleep(1)
turtle.clear()

turtle.goto(-50,0)
turtle.write("1...", move=False, align="left", font=("Arial", 50, "bold"))
time.sleep(1)
turtle.clear()

turtle.write("2..", move=False, align="left", font=("Arial", 50, "bold"))
time.sleep(1)
turtle.clear()

turtle.write("3!!!", move=False, align="left", font=("Arial", 50, "bold"))
time.sleep(1)
turtle.clear()
bgpic("doggi.gif")

###################################################################################

## PART 5: MOVEAROUND

def movearound(event):

	NEW_X_coordinate = event.x - screen_width
	NEW_Y_coordinate = -(event.y - screen_height)
	my_ball.goto(NEW_X_coordinate, NEW_Y_coordinate)


## PART 5.1: MOVE IT!

turtle.getcanvas().bind("<Motion>", movearound)
turtle.listen()


	
###################################################################################

## PART 6: THE WHILE LOOPEE

while running == True:
	if screen_width!=turtle.getcanvas().winfo_width()/2 or screen_height!=turtle.getcanvas().winfo_height()/2 :
		screen_width=turtle.getcanvas().winfo_width()/2 
		screen_height=turtle.getcanvas().winfo_height()/2


	move_all_balls()
	check_myball_collision()
	turtle.clear()
	turtle.color("white")
	turtle.goto(-800,300)
	turtle.write("score: "+str(score),font =('arial',20,'bold'))

	
	getscreen().update()
	time.sleep(sleep)
	


###################################################################################