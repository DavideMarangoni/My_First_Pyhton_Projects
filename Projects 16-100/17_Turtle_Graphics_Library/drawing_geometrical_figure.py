# l'esercizio consiste nel fare disegnare alla tartaruga:
# triangolo, quadrato, pentagono, esagono, ettagono, ottagono, nonagono, decagono
#consecutivamente l'uno all'altro e con colori diversi
from turtle import Turtle, Screen
from random import choice

colors = ["red", "blue", "purple", "green", "orange", "black", "yellow", "brown", "gold", "light blue"]

t = Turtle()

#triangle
t.color("black")
t.width(2)
t.speed('normal')

#mio metodo senza funzioni

# angle = 360
# angle_number = 3
# final_angle = 0
# while angle_number <= 10:
#     t.pencolor(choice(colors))
#     final_angle = angle/angle_number
#     for _ in range(angle_number):
#         t.right(final_angle)
#         t.forward(80)
#     angle_number += 1


# metodo con la funzione
def figure_shape(n_shape):
    angle = 360/n_shape
    for _ in range(n_shape):
        t.right(angle)
        t.forward(80)
for number_shape_n in range(3,11):
    t.color(choice(colors))
    figure_shape(number_shape_n)

screen = Screen()
screen.exitonclick()