from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

#Creo i miei oggetti
screen = Screen()
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.setup(width=600, height=600) #inizializzo le dimensioni delle mia finestra
screen.bgcolor("light green") #setto il colore dello sfondo del mio schermo
screen.title("Welcome to my Snake Game") #Inserisco il titolo del mia nuova finestra
screen.tracer(0) #.tracer serve a non far aggiornare lo schermo fino a quando non uso la funzione .update() serve per evitare animazioni

screen.update()

screen.listen()
screen.onkey(key="w", fun=snake.left)
screen.onkey(key="d", fun=snake.right)
screen.onkey(key="w", fun=snake.up)
screen.onkey(key="s", fun=snake.down)

game_is_on = True

while game_is_on:
    screen.update() #qui lo schermo si aggiorna, quindi in pratica non ho mostrato a schermo la creazione dei segmenti e il loro spostamento
    time.sleep(0.08)#rallento l'aggiornamento dello schermo di 0.15 secondi, quindi determina lka velocità del serpente
    snake.move()
    if snake.head.distance(food) < 20:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # implemento la collisione con il muro perimetrale della finestra
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

    # implemento la collisione con il corpo del serpente
    #In pseudo codice
    #Se la testa sbatte contro qualsiasi parte del corpo:
        #il gioco termina
        #Stampo Game Over

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
