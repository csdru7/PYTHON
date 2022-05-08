import turtle
from turtle import*
#screen for output
screen = turtle.Screen()
screen.setup(550, 600, startx=0, starty=100) 

# Defining a turtle Instance
t = turtle.Turtle()
 
# initially penup()
t.penup()
t.goto(-250, 250)
t.pendown()
t.speed(10)
 
# Orange Rectangle
#white rectangle
t.color("orange")
t.begin_fill()
t.forward(400)
t.right(90)
t.forward(100)
t.right(90)
t.forward(400)
t.end_fill()
t.penup()
t.goto(-250,50)
t.pendown()
t.left(90)

 
# Green Rectangle
t.color("green")
t.begin_fill()
t.forward(100)
t.left(90)
t.forward(400)
t.left(90)
t.forward(100)
t.end_fill()
 
# Big Blue Circle
t.penup()
t.goto(-5, 100)
t.pendown()
t.color("navy")
t.begin_fill()
t.circle(45)
t.end_fill()
 
# Big White Circle
t.penup()
t.goto(-9, 100)
t.pendown()
t.color("white")
t.begin_fill()
t.circle(40)
t.end_fill()
 
# Mini Blue Circles
t.penup()
t.goto(-83, 95)
t.pendown()
t.color("navy")

# Small Blue Circle
t.penup()
t.goto(-40, 100)
t.pendown()
t.begin_fill()
t.circle(10)
t.end_fill()
# Spokes
t.penup()
t.goto(-50, 100)
t.pendown()
t.pensize(2)
for i in range(24):
    t.forward(40)
    t.backward(40)
    t.left(15)
t.color("gray")
t.begin_fill()
t.penup()
t.goto(-250,250)
t.pendown()
t.left(90)
t.forward(20)
t.left(90)
t.forward(800)
t.left(90)
t.forward(20)
t.left(90)
t.forward(800)
t.end_fill()


     
#to hold the
#output window
turtle.done()