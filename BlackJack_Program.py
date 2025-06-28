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
    import random

    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]  # 10 = J/Q/K, 11 = Ace

    def user_take_card():
        return input("Type 'y' to get another card, type 'n' to pass: ") == 'y'

    def calculate_score(card_list):
        score = sum(card_list)
        # Gestione dell'asso
        if 11 in card_list and score > 21:
            card_list[card_list.index(11)] = 1
            score = sum(card_list)
        return score
    print("\n" * 30)
    print(logo)
    print("Welcome to Blackjack!")

    # User setup
    user_cards = [random.choice(cards), random.choice(cards)]
    computer_cards = [random.choice(cards)]
    game_over = False

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"\nYour cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 21:
            print("Blackjack! You win! 😁")
            game_over = True
        elif user_score > 21:
            print("You went over. You lose 😭")
            game_over = True
        else:
            if user_take_card():
                user_cards.append(random.choice(cards))
            else:
                game_over = True

    # Computer turn
    while calculate_score(computer_cards) < 17:
        computer_cards.append(random.choice(cards))

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f"\nYour final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

    if user_score > 21:
        print("You lose 😭")
    elif computer_score > 21 or user_score > computer_score:
        print("You win 😁")
    elif computer_score == user_score:
        print("It's a draw 😐")
    else:
        print("You lose 😤")


while continue_game():
    play_game()
input("Press ENTER for close game ")

