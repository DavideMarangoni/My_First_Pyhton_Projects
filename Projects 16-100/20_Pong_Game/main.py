from turtle import Screen
from gameboard import GameBoard
from paddle import Paddle
import time
from ball import Ball

# Set up screen
screen = Screen()
screen.setup(width=720, height=480)
screen.bgcolor("black")
screen.title("Welcome to my pong game")

screen.tracer(0)

# game objects
gameboard = GameBoard()
paddle = Paddle()
ball = Ball()

# input
screen.listen()
screen.onkey(paddle.user_move_up, "w")
screen.onkey(paddle.user_move_down, "s")


game_is_on = True
while game_is_on:
    screen.update()  # aggiorna lo schermo una volta che tutti gli elementi del gioco sono stati creati
    time.sleep(0.02)
    ball.move()

    # Rimbalzo paddle utente
    for segment in paddle.user_segments:
        if ball.distance(segment) < 20:
            new_angle = 180 - ball.heading()
            ball.setheading(new_angle % 360)

    # Rimbalzo paddle PC
    for segment in paddle.pc_segments:
        if ball.distance(segment) < 20:
            new_angle = 180 - ball.heading()
            ball.setheading(new_angle % 360)

    #gestisco se la palla va oltre il paddle avversario facendo segnare il punto all'utente
    if ball.xcor() > 360:
        gameboard.increase_user_score()
        ball.random_move()
        ball.move()

    #se la palla va oltre il paddle utente, segna il punto dell'avversario
    elif ball.xcor() < -360:
        gameboard.increase_opponent_score()
        ball.random_move()
        ball.move()

    # Rimbalzo sui muri alto e basso
    if ball.ycor() > 230 or ball.ycor() < -230:
        new_angle = 360 - ball.heading()
        ball.setheading(new_angle % 360)

    # stabilisco il punteggio da raggiungere per terminare la partita (10 punti)
    if gameboard.user_score == 10:
        game_is_on = False
        gameboard.end_game_user()
    elif gameboard.opponent_score == 10:
        game_is_on = False
        gameboard.end_game_opponent()

    paddle.pc_follow_ball(ball)


screen.exitonclick()