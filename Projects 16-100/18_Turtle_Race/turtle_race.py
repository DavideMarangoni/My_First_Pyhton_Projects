import turtle
from turtle import Turtle, Screen
import random as r


is_on_race = False
screen = Screen()
screen.setup(500,400)
user_bet = screen.textinput(title="Make yur bet", prompt="Which turtle will win the race? Enter a color: ").lower()
print(f"You choose the {user_bet} turtle, good luck!")
colors =["red", "green", "purple", "blue", "yellow", "orange"]
all_turtles = []

y = -100
for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.speed("slow")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-230, y= y)
    y += 40
    all_turtles.append(new_turtle)

if user_bet:
    is_on_race = True

while is_on_race:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_on_race = False
            winner_color = turtle.color()
            if str(winner_color[0]) == user_bet:
                print("You win the race!!" )
            else:
                print(f"The {winner_color[0]} turtle won the race. You lose... ")
        else:
            random_distance =  r.randint(1, 10)
            turtle.forward(random_distance)

screen.exitonclick()
