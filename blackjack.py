# Name: Ruben Sanduleac
# Date: January 22nd, 2022
# Description: Blackjack is a game that is played using cards.
# The gaol of the game is to add up the cars to the largest number without going over twenty-one.
# If the cards in the hand add up more than twenty-one then its called a bust.
# Meaning the game is lost imidiatly. It doesent matter how much the user goes over twenty one then the user looses.
# The way the cards are counted are that all the cards from 2 - 10 are counted as their face value.
# The Jack, Queen, and King cards count as ten. The Ace card can count as 1 to the total or can count as 11.
# Depending if the user went over 21 or under the user can decide the value of the Ace.


import random


def deal_card():
    # list of cards in the deck
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def cal_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has a Blackjack"
    elif user_score == 0:
        return "You Win!"
    elif user_score > 21:
        return "You went over"
    elif computer_score > 21:
        return "Opponet went over"
    elif user_score > computer_score:
        return "You Win"
    else:
        return "You Lose"


def game():
    # user cards cards
    user_cards = []
    # user cards cards
    computer_cards = []

    game_over = False

    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = cal_score(user_cards)
        computer_score = cal_score(computer_cards)

        print(f"    Your cards: {user_cards}, current score: {user_score}")
        print(f"    Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            continue_deal = input(
                "Type 'y' to get another card, type 'n' to pass: ").lower()
            if continue_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = cal_score(computer_cards)

    print(f" Your cards: {user_cards}, final score: {user_score}")
    print(
        f" Computer's final cards: {computer_cards}, final score: {computer_score}")
    compare(user_score, computer_score)


while input("Type 'y' to play another round, or type 'n' to to exit") == 'y':
    game()
