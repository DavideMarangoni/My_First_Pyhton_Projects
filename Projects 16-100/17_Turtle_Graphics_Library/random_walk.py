#Generare una random walk infinita con la libreria Turtle
from turtle import Turtle, colormode, Screen
from random import choice, randint

colormode(255)
tim = Turtle('arrow')
tim.speed('fast')
tim.width(5)
screen = Screen()
go = True

def random_color():
    """Return a random color"""
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    generated_color = (r, g, b)
    return generated_color

def move():
    while go:
        tim.forward(25)
        tim.pencolor(random_color())
        tim.right(choice((90,180,270,360)))


move()
screen.mainloop()