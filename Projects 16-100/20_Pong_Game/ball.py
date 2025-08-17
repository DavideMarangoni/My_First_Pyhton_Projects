from turtle import Turtle
from random import randint, choice

BALL_SPEED = 10


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.random_angle = 0
        self.shape("circle")
        self.color("red")
        self.penup()
        self.random_move()


    def random_ball_position(self):
        random_y = randint(-100, 100)
        self. goto(x=0, y=random_y)

    def random_move(self):

        self.random_ball_position()
        random_direction = choice([0, 1])

        if random_direction == 0:
            self.random_angle = randint(150,210)
            self.setheading(self.random_angle)
        else:
            self.random_angle = randint(-30, 30)
            self.setheading(self.random_angle)

    def move(self):
        self.forward(BALL_SPEED)



