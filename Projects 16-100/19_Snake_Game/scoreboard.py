from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 18, 'bold')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 265)
        self.color("Dark Blue")
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT )

    def increase_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0,-10)
        self.write(f"GAME OVER!", align=ALIGNMENT, font=('Courier', 22, 'bold'))