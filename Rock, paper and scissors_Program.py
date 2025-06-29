import random
import sys
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("Welcome to the paper, rock and scissors game!!!\nAre you reade?!\nLet's gooo")
direction = "yes"
draw = "True"
while direction == "yes":
    while draw == "True":
        # Faccio prendere una decisione all'utente
        user_choice = input("What do you choose? Type Rock, Paper or Scissors.\n")
        print("\nYou chose:")
        if user_choice.lower() == "rock":
            print(rock)
        elif user_choice.lower() == "paper":
            print(paper)
        elif user_choice.lower() == "scissors":
            print(scissors)
        else:
            print("You enter a wrong input...\nYou lose! ")
            exit()

        # Faccio prendere una decisione random al computer
        print("\nComputer chose:")
        game_list = ["rock", "paper", "scissors"]
        computer_choice = random.choice(game_list)
        if computer_choice == "rock":
            print(rock)
        elif computer_choice == "paper":
            print(paper)
        else:
            print(scissors)

        # Imposto le condizioni della vittoria dell'utente o del computer
        # if user_choice = rock
        if user_choice == "rock"  and computer_choice == "rock":
            print("It's a draw...")
        elif user_choice == "rock" and computer_choice == "paper":
            print("You lose...")
            draw = "False"
        elif user_choice == "rock" and computer_choice == "scissors":
            print("You win!")
            draw = "False"

        # if user_choice = paper
        if user_choice == "paper"  and computer_choice == "rock":
            print("You win!")
            draw = "False"
        elif user_choice == "paper" and computer_choice == "paper":
            print("It's a draw...")
        elif user_choice == "paper" and computer_choice == "scissors":
            print("You lose...")
            draw = "False"

        # if user_choice = scissors
        if user_choice == "scissors"  and computer_choice == "rock":
            print("You lose...")
            draw == "False"
        elif user_choice == "scissors" and computer_choice == "paper":
            print("You win!")
            draw = "False"
        elif user_choice == "scissors" and computer_choice == "scissors":
            print("It's a draw...")
        print("\n"*20)
    direction = input("Do you want to do another game? (type 'yes' or 'no'): ").lower()
    if direction == "yes":
        direction = "yes"
        draw = "True"
    else:
        direction = "no"
input("\npress ENTER for finish")















