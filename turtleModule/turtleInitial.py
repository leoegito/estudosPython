from turtle import *
the_turtle = Turtle()

the_turtle.shape("turtle")
the_turtle.color("red")

for i in range(0,4):
    the_turtle.forward(100)
    the_turtle.right(90)

screen = Screen()
screen.exitonclick()