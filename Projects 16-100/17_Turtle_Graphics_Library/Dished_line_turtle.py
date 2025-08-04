# L'esercizio consiste nel far disegnare alla tartaruga una linea tratteggiata
# Io ho cambiato l'esercizio in modo che disegni un quadrato tratteggiato
from turtle import Turtle, Screen

t = Turtle()

for i in range(4):
    for _ in range(15):
        t.forward(10)
        t.penup() #gli dico di alzare la penna, quindi non disegnerà
        t.forward(10)
        t.pendown() #gli dico di riabbassare la penna, ora scrive
    t.left(90)

screen = Screen()
screen.exitonclick()
