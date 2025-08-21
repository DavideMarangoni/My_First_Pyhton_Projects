from turtle import Screen
import time
from player import Player
from board import Board
from graphics import Street
from cars import Car

# start the setup screen
screen = Screen()

# screen setup
screen.setup(width= 600, height=600)
screen.bgcolor("light green")

screen.tracer(0)

# game objects
player = Player()
board = Board()
street = Street()
car = Car()

#game inputs
screen.listen()
screen.onkey(key="w", fun=player.move)

game_is_on = True

while game_is_on:

    screen.update()
    time.sleep(0.1)
    car.create()
    car.move()

    if player.ycor() > 240:
        board.update_score()
        player.new_level()
        car.increase_speed()

    for ferrari in car.cars:
        if player.distance(ferrari) < 24:
            game_is_on = False


screen.exitonclick()