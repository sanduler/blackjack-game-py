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

start = input(
    "Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
print(start)

# list of cards in the decl
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# user cards cards
user_cards = []
# user cards cards
computer_cards = []
comp_length = len(computer_cards)
user_length = len(user_cards)

# start the user and the computer with two cards in the hand.
for i in range(2):
    user_cards.append(random.choice(cards))
    computer_cards.append(random.choice(cards))

computer_total = 0

for comp_length in computer_cards:
    # print(computer_cards)
    # print(comp_length)
    # # print(computer_cards[comp_length])
    computer_total += comp_length
print(computer_total)

user_total = 0
for user_length in user_cards:
    user_total += user_length
print(user_total)

print(f"Your cards: {user_cards}, current score: {user_total}")
print(f"Computer's first card: {computer_cards[0]}")
input("Type 'y' to get another card, type 'n' to pass:")


# TODO Deal both user and computer a starting hand of 2 random card values.

# TODO Detect when computer or user has a blackjack. (Ace + 10 value card).
# TODO If computer gets blackjack, then the user loses (even if the user also has a blackjack).
# If the user gets a blackjack, then they win (unless the computer also has a blackjack).
# TODO Calculate the user's and computer's scores based on their card values.
# TODO If an ace is drawn, count it as 11. But if the total goes over 21, count the ace as 1 instead.
# TODO Reveal computer's first card to the user.
# TODO Game ends immediately when user score goes over 21 or if the user or computer gets a blackjack.
# TODO Ask the user if they want to get another card.
# TODO Once the user is done and no longer wants to draw any more cards, let the computer play.
# The computer should keep drawing cards unless their score goes over 16
# TODO Compare user and computer scores and see if it's a win, loss, or draw.
# TODO Print out the player's and computer's final hand and their scores at the end of the game.
# TODO After the game ends, ask the user if they'd like to play again. Clear the console for a fresh start.
