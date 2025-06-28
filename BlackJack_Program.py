logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def continue_game():
    """
    Ask to the user if he wants to do a game.
    True if "y"
    False if "y"
    """
    cont = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if cont == "y":
        return True
    else:
        return False
def user_take_card():
    take_card = input("Type 'y' to get another card, type 'n' to pass: ")
    if take_card == "y":
        return True
    else:
        return False
def play_game():
    print("\n"*30)
    print(logo)
    pc_random_list = []
    pc_rand_card = random.choice(cards)
    pc_random_list.append(pc_rand_card)
    score_computer = 0
    for numero in pc_random_list:
        score_computer += numero

    user_rand_list = []
    user_rand_card_1 = random.choice(cards)
    user_rand_card_2 = random.choice(cards)
    user_rand_list.append(user_rand_card_1)
    user_rand_list.append(user_rand_card_2)
    score_user = 0
    for numero in user_rand_list:
        score_user += numero
    if score_user == 21:
        print("You win with a BlackJack! 😁")
    else:
        print(f"Your cards: {user_rand_list}, current score: {score_user} ")
        print(f"Computer's first card: {pc_rand_card}")
        while user_take_card():
            new_card = random.choice(cards)
            score_user += new_card
            user_rand_list.append(new_card)
            if score_user > 21:
                print(f"Your final hand: {user_rand_list}, final score: {score_user}")
                print(f"Computer's final hand: {pc_random_list}, final score: {score_computer}")
                print("You went over. You lose 😭 ")
            else:
                print(f"Your cards: {user_rand_list}, current score: {score_user}")
        while score_computer <= 17:
            new_card = random.choice(cards)
            pc_random_list.append(new_card)
            score_computer += new_card
        if score_computer > 21:
                print(f"Your final hand: {user_rand_list}, final score: {score_user}")
                print(f"Computer's final hand: {pc_random_list}, final score: {score_computer}")
                print("Opponent went over. You win 😁")
        else:
            if score_computer > score_user:
                print(f"Your final hand: {user_rand_list}, final score: {score_user}")
                print(f"Computer's final hand: {pc_random_list}, final score: {score_computer}")
                print("You lose 😤 ")
            elif score_computer == score_user:
                print(f"Your final hand: {user_rand_list}, final score: {score_user}")
                print(f"Computer's final hand: {pc_random_list}, final score: {score_computer}")
                print("It's a draw 😤 ")
            elif score_computer < score_user:
                print(f"Your final hand: {user_rand_list}, final score: {score_user}")
                print(f"Computer's final hand: {pc_random_list}, final score: {score_computer}")
                print("You win 😃 ")

while continue_game():
    play_game()
input("Press ENTER for close game ")

