from sys import exit

print("Welcome to Python Pizza Deliveries!\n")
bill = 0

# ask what size of pizza the user wants
size = input("What size pizza do you want? S, M or L: ")
if size.lower() == "s":
    bill = 15
elif size.lower() == "m":
    bill = 20
elif size.lower() == "l":
    bill = 25
else:
    print("Your input is wrong ")
    exit()

# ask pepperoni at the user
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
if pepperoni.lower() == "y":
    if size.lower() == "s":
        bill += 2
    elif size.lower() == "m" or size.lower() == "l":
        bill += 3
if pepperoni.lower() != "n" and pepperoni.lower()!= "y":
    print("Your input is wrong ")
    exit()

# ask if user wants extra cheese
extra_cheese = input("Do you want extra cheese? Y or N: ")
if extra_cheese.lower() == "y":
    bill += 1
if extra_cheese.lower() != "n" and extra_cheese.lower() != "y":
    print("Your input is wrong ")
    exit()

print(f"\nYour final bill is: ${bill}")
input("\npress ENTER for finish")

