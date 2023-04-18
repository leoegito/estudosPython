from turtle import Turtle, Screen
from time import time
import random

#still incomplete - late night
screen = Screen()
screen.setup(width=600, height=400)
user_turtle = screen.textinput(title="Turtle Race! Who will win? Competitors: red, blue, yellow, purple, orange, green", prompt="Which turtle will win the race? Enter the color: ")
# List of available turtles
colors = ["red", "blue", "yellow", "purple", "orange", "green"]
competitors = []
# Logic of the program
##
x_pos = -280
y_pos = 150
for competitor in colors:
    turtle = Turtle(shape="turtle")
    turtle.color(competitor)

    y_pos -= 40
    turtle.penup()
    turtle.goto(x=x_pos, y=y_pos)

    competitors.append(turtle)

# time_count = time.perf_counter()
while True:
    foward_one = random.choice(competitors)
    foward_one.forward(28)
    if foward_one.xcor() >= 280:
        break
    
screen.exitonclick()
