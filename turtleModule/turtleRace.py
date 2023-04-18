from turtle import Turtle, Screen
import time
import random

# Screen setup
screen = Screen()
screen.setup(width=600, height=400)

# List of available turtles
colors = ["red", "blue", "yellow", "purple", "orange", "green"]

# User input. Repeat until is valid
while True:
    user_turtle = screen.textinput(title="Turtle Race! Who will win? Competitors: red, blue, yellow, purple, orange, green", prompt="Which turtle will win the race? Enter the color: ")
    if user_turtle in colors:
        break
    
# List of turtles instances, will be added in the next loop
competitors = []

# Initial position of the screen where the turtles will spawn
x_pos = -280
y_pos = 150

for competitor in colors:
    turtle = Turtle(shape="turtle")
    turtle.color(competitor)

    y_pos -= 40
    turtle.penup()
    turtle.goto(x=x_pos, y=y_pos)

    competitors.append(turtle)

# Race logic starts here
while True:
    foward_one = random.choice(competitors)
    foward_one.forward(20)
    # if you need to slow down the race a little bit, remove the hash below:
    # time.sleep(0.1)
    if foward_one.xcor() >= 280:
        winner = foward_one
        break

if winner.fillcolor() == user_turtle:
    screen.clearscreen()
    winner.goto(0, 0)
    winner.write("You Won! Congratulations!", True, align="center", font=('Verdana', 12, 'bold'))
else:
    for loser in competitors:
        if loser.fillcolor() == user_turtle:
            loser.goto(0, 0)
            loser.write("Sorry bro! Didn't make it in time. Next time i'll try harder!", True, align="center", font=('Arial Black', 12, 'bold'))
            break

# End
screen.exitonclick()
