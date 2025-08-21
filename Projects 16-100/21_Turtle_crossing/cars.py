from turtle import Turtle
from random import choice, randint

CARS_COLOR = ["green", "red", "blue", "purple", "brown", "yellow", "pink"]
CARS_POSITION = [[300, -205], [300, -175], [300, -115], [300, -85], [300, -25],
                 [300, 5], [300, 95], [300, 65], [300, 185], [300, 155]]
STARTING_MOVE_DISTANCE = 10
MOVE_INCREMENT = 4
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create(self):

        if randint(1, 4) == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=3)  # rettangolo
            new_car.penup()
            new_car.color(choice(CARS_COLOR))
            random_y = choice(CARS_POSITION)[1]
            new_car.goto(SCREEN_WIDTH // 2, random_y)
            self.cars.append(new_car)

    def move(self):

        for car in self.cars:
            car.backward(self.car_speed)

    def increase_speed(self):
        """Aumenta la velocità (quando il giocatore avanza di livello)"""
        self.car_speed += MOVE_INCREMENT





