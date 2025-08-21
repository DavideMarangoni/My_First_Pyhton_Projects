from turtle import Turtle

START_POSITION = (0, -280)
MOVE_DISTANCE = 20

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(START_POSITION)
        self.setheading(90)
        self.color("red")

    def move(self):
        self.forward(MOVE_DISTANCE)

    def new_level(self):
        self.goto(START_POSITION)