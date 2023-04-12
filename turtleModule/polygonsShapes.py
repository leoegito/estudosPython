import turtle as t
import random

turtle = t.Turtle()

colours = ["yellow", "gold", "orange", "red", "crimson", "violet", "magenta", "purple", "indigo", "blue", "lavender", "slate blue", "aquamarine", "green", "dark green", "brown", "gray"]

for n_sides in range(3, 11):
    angle = 360 / n_sides
    turtle.color(random.choice(colours))
    for _ in range(n_sides):
        turtle.forward(100)
        turtle.right(angle)