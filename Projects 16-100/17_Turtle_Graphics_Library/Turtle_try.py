# importo la libreria Turtle e screen
from turtle import Turtle, Screen

turtle = Turtle() # Creo il mio oggetto
turtle.shape("arrow")
turtle.color("black")
turtle.fillcolor("red")

turtle.forward(100) # gli dico di muoversi di 100 pixel
turtle.right(90) #gli dico di girare a destra di 90°

turtle.begin_fill() #gli dico di iniziare il riempimento
turtle.circle(50) # gli dico di fare un cerchio di 50 radianti
turtle.circle(-50)
turtle.end_fill() # termina il riempimento



screen = Screen()
screen.exitonclick()