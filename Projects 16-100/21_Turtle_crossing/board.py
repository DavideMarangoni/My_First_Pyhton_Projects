from idlelib.configdialog import FontPage
from turtle import Turtle

SCORE_POSITION = (-220, 260)
SCORE_FONT = ('Courier', 18, 'bold')
ALIGNMENT = "center"

class Board(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level = 0
        self.penup()
        self.goto(SCORE_POSITION)
        self.update_score()

    def update_score(self):
        self.clear()
        self.increase_level()
        self.write(f"Level: {self.level}", font= SCORE_FONT, align=ALIGNMENT)

    def increase_level(self):
        self.level += 1