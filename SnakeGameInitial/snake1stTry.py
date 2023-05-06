from turtle import Screen, Turtle
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Classic Snake Game")

def move_forward(obj):
    obj.forward(10)

def move_backwards(cursor):
    cursor.backward(10)

def move_left(cursor):
    cursor.setheading(cursor.heading()+10)

def move_right(cursor):
    cursor.setheading(cursor.heading()-10)

def clear(cursor):
    cursor.clear()
    cursor.penup()
    cursor.home()
    cursor.pendown()
    return cursor

#Challenge
snakeHead = Turtle()
snakeHead.color("white")
snakeHead.shape("square")
snakeHead.goto(0,0)

food = Turtle()
food.color("black")
food.shape("square")
food.penup()
food.goto(random.randint(-290,290), random.randint(-290,290))
food.shapesize(0.75, 0.75, 1)
food.color("red")

snake = [snakeHead]
print(snakeHead)
print(snake)

# sets a listener for the screen, to capture the keypressed
screen.listen()
screen.onkey(move_forward(snakeHead), "w")
screen.onkey(move_backwards(snakeHead), "s")
screen.onkey(move_left(snakeHead), "a")
screen.onkey(move_right(snakeHead), "d")
screen.onkey(clear(snakeHead), "c")
screen.exitonclick()