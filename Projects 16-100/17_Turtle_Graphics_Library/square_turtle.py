# Lo scopo dell'esercizio è far disegnare alla tartaruga un quadrato di qualsiasi tipo
from turtle import Turtle, Screen

t = Turtle()
t.shape("arrow")
t.color("black", "DarkViolet")

t.begin_fill()

for i in range(2):
    t.forward(200)
    t.left(90)
for i in range(3):
    t.forward(400)
    t.left(90)
t.forward(200)

t.end_fill()

screen = Screen()
screen.exitonclick()