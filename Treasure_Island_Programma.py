print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
from sys import exit
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

print("You're at a cross road. Where do you want to go?")
a = input("\tType 'right' or 'left'\n")
if a != "left":
    print("You fell into a hole. Game Over.")
    exit()
else:
    print("You've come to a lake. There is an island in the middle of the lake.")
    b = input("\tType 'wait' to wait for a boat. Type 'swim' to swim across.\n")
if b != "wait":
    print("You get attacked by an angry trout. Game Over.")
    exit()
else:
    print("You arrive at the island unharmed. There is a house with 3 doors.")
    c = input("\tOne red, one yellow and one blue. Which colour do you choose?\n")
if c == "red":
    print("It's a room full of fire. Game Over.")
    exit()
elif c == "blue":
    print("You enter a room of beasts. Game Over.")
    exit()
else:
    print("\n          __________")
    print("         /         /|")
    print("        /_________/ |")
    print("        |         | |")
    print("        |  $$$$$  | |")
    print("        | $$$$$$$ | |")
    print("        |__$$$$$__|/ ")
    print("       /__________/ ")
    print("      |   GOLD!   | ")
    print("      |___________| ")
    print("\nYou found the treasure! You Win!\n")

    input("\npress ENTER for finish")