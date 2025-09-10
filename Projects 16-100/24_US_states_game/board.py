import time
from turtle import Turtle

SCORE_POSITION = (0, 270)
ALIGNMENT = "center"
FONT = ("Arial", 20, "bold")

class Board(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.speed("fastest")
        self.penup()
        self.goto(SCORE_POSITION)
        self.increase_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}/50 states guessed", font=FONT, align= ALIGNMENT)

    def increase_score(self):
        self.update_score()
        self.score += 1


