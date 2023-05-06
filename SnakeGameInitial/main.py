from turtle import Screen, Turtle
import random
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Classic Snake Game")
screen.tracer(0)

startingPositions = [(0,0),(-20,0),(-40,0)]

snake = []

for position in startingPositions:
    segment = Turtle()
    segment.penup()
    segment.color("white")
    segment.shape("square")
    segment.goto(position)
    snake.append(segment)

gameIsOn = True

while gameIsOn:
    screen.update()
    time.sleep(0.1)
    # for seg in snake:
    #     seg.forward(20)
    for segNumber in range(len(snake)-1,0,-1):
        new_x = snake[segNumber-1].xcor()
        new_y = snake[segNumber-1].ycor()
        snake[segNumber].goto(new_x,new_y)
    snake[0].forward(20)


# food = Turtle()
# food.color("black")
# food.shape("square")
# food.penup()
# food.goto(random.randint(-290,290), random.randint(-290,290))
# food.shapesize(0.75, 0.75, 1)
# food.color("red")

screen.exitonclick()