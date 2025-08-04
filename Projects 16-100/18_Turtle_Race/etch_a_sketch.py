from turtle import Turtle, Screen, colormode


tim = Turtle()
screen = Screen()
tim.shape("turtle")

def move_forwards():
    tim.forward(30)
def move_backwards():
    tim.backward(30)
def turn_left():
    tim.left(20)
def turn_right():
    tim.right(20)
def clear_all():
    tim.clear()
    tim.teleport(0,0)
    tim.setheading(0)

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear_all)

screen.exitonclick()


