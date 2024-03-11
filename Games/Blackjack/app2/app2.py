import random
from art import logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

players_card = random.randint(1,11)
computers_card = random.randint(1,11)

players_hand = []
computers_hand = []

players_hand.append(players_card)
players_card = random.randint(1,11)
players_hand.append(players_card)
computers_hand.append(computers_card)
computers_card = random.randint(1,11)
computers_hand.append(computers_card)
players_score = 0
computers_score = 0
for card in players_hand:
    players_score += card
for card in computers_hand:
    computers_score += card


keep_playing = True
while keep_playing == True:
    print(logo)
    print(f"Your cards: {players_hand}, current score: {players_score}")
    print(f"Computer's first card: [{computers_hand[0]}]")
    choice = input("Type 'y' to get another card, type 'n' to pass:").lower()
    if choice == 'y':
        players_card = random.randint(1,11)
        players_hand.append(players_card)
        new_cards = 0
        for card in players_hand:
            new_cards += card
        players_score = new_cards 
        if new_cards > 21:
            keep_playing = False
            print(f"Your cards: {players_hand} Your Score: {players_score}")
            print("You went over 21. You Lose")
            print(f"Computer's hand: [{computers_hand}] Computer's final Score: {computers_score}")
        elif players_score == 21:
            keep_playing = False
            print("BLACKJACK: YOU WIN!!!")
            print(f"Your cards: {players_hand} Your Score: {players_score}")
            print(f"Computer's hand: [{computers_hand}] Computer's final Score: {computers_score}")
    if choice == 'n':
        if computers_score == 21:
            keep_playing = False
            print("You lose the computer got 21.")
            print(f"Computer's hand: [{computers_hand}] Computer's final Score: {computers_score}")
        elif computers_score < 17:
            while computers_score <17:
                temp_score = 0
                computers_card = random.randint(1,11)
                computers_hand.append(computers_card)
                for card in computers_hand:
                    temp_score += card
                    if temp_score >= 17:
                        computers_score = temp_score
        elif computers_score >21:
            keep_playing = False
            print("You win the computer went over 21.")
            print(f"Computer's hand: [{computers_hand}] Computer's final Score: {computers_score}")
        elif players_score == computers_score:
            keep_playing = False
            print("DRAW:")
            print(f"Computer's hand: [{computers_hand}] Computer's final Score: {computers_score}")
        elif computers_score > players_score:
            keep_playing = False
            print("You lose the computer is closer to 21.")
            print(f"Computer's hand: [{computers_hand}] Computer's final Score: {computers_score}")
        elif computers_score < players_score:
            keep_playing = False
            print("You Win you are closer to 21.")
            print(f"Computer's hand: [{computers_hand}] Computer's final Score: {computers_score}")
    
 
