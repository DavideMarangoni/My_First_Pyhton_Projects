from turtle import Turtle

SCORE_FONT = ('Courier', 40, 'bold')
END_FONT = ('Courier', 30, 'bold')
ALIGNMENT = "center"

USER_SCORE_POSITION = (-70, 180)
OPPONENT_SCORE_POSITION = (70, 180)
END_POSITION = (-10, 0)
CENTRAL_LINE_POSITION = (0,240)

class GameBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.user_score = 0
        self.opponent_score = 0
        self.update_score()
        self.central_line()

    def central_line(self):
        self.hideturtle()
        self.penup()
        self.goto(CENTRAL_LINE_POSITION)
        self.pencolor("white")
        self.pensize(4)
        self.setheading(270)
        for trattino in range(25):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)

    def update_score(self):
        self.clear()
        self.goto(USER_SCORE_POSITION)
        self.write(f"{self.user_score}", align=ALIGNMENT, font=SCORE_FONT)
        self.goto(OPPONENT_SCORE_POSITION)
        self.write(f"{self.opponent_score}", align=ALIGNMENT, font=SCORE_FONT)

    def increase_user_score(self):
        self.user_score += 1
        self.update_score()
        self.central_line()

    def increase_opponent_score(self):
        self.opponent_score += 1
        self.update_score()
        self.central_line()

    def end_game_user(self):
        self.clear()
        self.goto(END_POSITION)
        self.write("Complimenti, hai vinto!", align=ALIGNMENT, font=END_FONT)

    def end_game_opponent(self):
        self.clear()
        self.goto(END_POSITION)
        self.write("Mi spiace, hai perso!", align=ALIGNMENT, font=END_FONT)


