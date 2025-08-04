from turtle import Turtle, colormode, Screen
from random import randint
tim = Turtle()
tim.width(1)
tim.speed('fastest')
colormode(255)

def random_color():
    """Return a random color"""
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    generated_color = (r, g, b)
    return generated_color

for _ in range(60):
    tim.pencolor(random_color())
    tim.circle(150)
    tim.left(6)

screen = Screen()
screen.exitonclick()