from turtle import Screen, Turtle
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=400)
screen.bgcolor("black")
screen.title("Classic Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game = True
while game:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()