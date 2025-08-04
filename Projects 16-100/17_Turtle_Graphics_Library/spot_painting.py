from turtle import Turtle, Screen, colormode
from random import randint, choice
import colorgram
colors = colorgram.extract(r"C:\Users\david\OneDrive\Desktop\PYTHON\Udemy\My_First_Pyhton_Projects\Projects 16-100\17_Turtle_Graphics_Library\images.png", 8)
color_list = []
for i in range(8):
    r = colors[i].rgb.r
    g = colors[i].rgb.g
    b = colors[i].rgb.b
    tupla = (r,g,b)
    color_list.append(tupla)

tim = Turtle()

colormode(255)
tim.speed('fast')
tim.color("black")
tim.shape('arrow')
tim.pensize(20)
x = -300
y = -300

tim.teleport(x,y)

for line in range(11):
    for _ in range(11):
        tim.dot(20, choice(color_list))
        tim.penup()
        tim.forward(50)
    y += 50
    tim.teleport(x, y)

screen = Screen()
screen.exitonclick()