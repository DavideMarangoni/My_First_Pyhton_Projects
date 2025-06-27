logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
dic = {}
direction = "yes"
print("Welcome to the Davide's auction program!\n")
print("It's very simple: Type a name and a bid, at the end of program I'll able to tell you who is the winner\nLet's go\n")
while direction == "yes":
    # TODO-1: Ask the user for input
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    # TODO-2: Save data into dictionary {name: price}
    dic[name] = bid
    # TODO-3: Whether if new bids need to be added
    direction = input("Are there any other bidders? Type 'yes or 'no': ").lower()
    if direction == "yes":
        direction = "yes"
        print("\n" * 20)
    else:
        direction = "no"
# TODO-4: Compare bids in dictionary
max_bidder = 0
max_name_bidder = ""
for key in dic:
    if dic[key] > max_bidder:
        max_bidder = dic[key]
        max_name_bidder = key
print(f"The winner is {max_name_bidder} with a bid of ${max_bidder}")
input("\nPremi INVIO per chiudere...")


