from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("red")
        self.penup()
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)  # più piccola della testa del serpente
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """Riposiziona la mela in una posizione casuale sulla griglia."""
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)
