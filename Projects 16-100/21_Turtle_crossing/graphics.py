from turtle import Turtle

STREET_POSITION = [(-300, -220), (-300, -130), (-300, -40), (-300, 50), (-300, 140)]
DOTTED_LINE_POSITION = [(-300, -190), (-300, -100), (-300, -10), (-300, 80), (-300, 170)]

class Street(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.user_interface()

    def user_interface(self):

        for position in STREET_POSITION:
            self.goto(position)
            self.street()
        for line in DOTTED_LINE_POSITION:
            self.goto(line)
            self.dotted_line()

    def street(self):
        self.pendown()
        self.pencolor("black")
        self.begin_fill()
        for side in range(2):
            self.forward(600)
            self.left(90)
            self.forward(60)
            self.left(90)
        self.end_fill()
        self.penup()

    def dotted_line(self):
        self.pensize(3)
        self.color("grey")
        for p in range(12):
            self.pendown()
            self.forward(25)
            self.penup()
            self.forward(25)


