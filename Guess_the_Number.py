logo = r"""
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_| 
"""
import random
import sys
print(logo)
print("Welcome to the Number Guessin Game! ")
print("I'm thinking of a number between 1 and 100. ")
number = random.randint(0,100)
difficult = input("\nChoose a difficulty. Type 'easy' or 'hard': ").lower()
lives = 10
if difficult == "easy":
    lives = 10
    print(f"\nYou have {lives} attempts remaining to guess the number.")
elif difficult == "hard":
    lives = 5
    print(f"\nYou have {lives} attempts remaining to guess the number.")
user_guess = ""
while lives != 0:
    user_guess = int(input("\nMake a guess: "))
    if user_guess < number:
        print("Too low")
        lives -= 1
        print(f"\nYou have {lives} attempts remaining to guess the number.")
    elif user_guess > number:
        print("Too high")
        lives -= 1
        print(f"\nYou have {lives} attempts remaining to guess the number.")
    elif user_guess == number:
        print(f"\nYou got it! The answer was {number}")
        input("\nPress ENTER for close the program ")
        exit()
print("\nYou've run out of guesses, you lose. ")
