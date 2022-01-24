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

# user cards cards
user_cards = []
# user cards cards
computer_cards = []

game_over = False


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


user_score = cal_score(user_cards)
computer_score = cal_score(computer_cards)
print(f"    You cards: {user_cards}, current score: {user_score}")
print(f"    Computer's first card: {computer_cards[0]}")
if user_cards == 0 or computer_score == 0 or user_score > 21:
    is_game_over = True

    # # Deal both user and computer a starting hand of 2 random card values. (Done)
    # # Deal both user and computer a starting hand of 2 random card values. (Done)
    # # TODO Detect when computer or user has a blackjack. (Ace + 10 value card).
    # # TODO If computer gets blackjack, then the user loses (even if the user also has a blackjack).
    # # If the user gets a blackjack, then they win (unless the computer also has a blackjack).
    # # Calculate the user's and computer's scores based on their card values. (Done)
    # # TODO If an ace is drawn, count it as 11. But if the total goes over 21, count the ace as 1 instead.
    # #  Reveal computer's first card to the user. (Done)
    # # TODO Game ends immediately when user score goes over 21 or if the user or computer gets a blackjack.
    # # TODO Ask the user if they want to get another card.
    # # TODO Once the user is done and no longer wants to draw any more cards, let the computer play.
    # # The computer should keep drawing cards unless their score goes over 16
    # # TODO Compare user and computer scores and see if it's a win, loss, or draw.
    # # TODO Print out the player's and computer's final hand and their scores at the end of the game.
    # # TODO After the game ends, ask the user if they'd like to play again. Clear the console for a fresh start.
