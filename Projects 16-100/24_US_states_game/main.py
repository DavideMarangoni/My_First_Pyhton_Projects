import turtle
import pandas as pd
from board import Board

screen = turtle.Screen()
board = Board()


screen.title("U.S. States game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

df = pd.read_csv("50_states.csv")

# lista di stati in lowercase
state_names = [name.lower() for name in df["state"]]

# dizionario {stato: (x, y)}
state_coordinate = {row.state.lower(): (row.x, row.y) for _, row in df.iterrows()}

game_is_on = 0
guessed_states = []
states_to_learn = []

while game_is_on < 50:

    user_answer = screen.textinput(title="Guess the US State", prompt="What's another state's name?").lower()

    if user_answer == "exit":

        # states to learn list in csv
        states_to_learn = [state.capitalize() for state in state_names if state not in guessed_states]
        states_to_learn = pd.DataFrame(states_to_learn, columns=["State"])
        states_to_learn.to_csv("states_to_learn.csv")
        break

    elif user_answer in state_names:

        # recupero coordinate dello stato
        x, y = state_coordinate[user_answer]
        # creo una tartaruga per scrivere il nome
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(x, y)
        t.write(user_answer.title(), align="center", font=("Arial", 8, "bold"))
        board.increase_score()
        game_is_on += 1
        guessed_states.append(user_answer)