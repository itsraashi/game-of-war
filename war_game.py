# Source: Used Flask API documentation, as starting point for endpoints
# https://flask.palletsprojects.com/en/2.3.x/api/?highlight=routing

from flask import Flask
from table_functions import *
import random

app = Flask(__name__)

class Card():
    def __init__(self, suit, card_name, value):
        self.suit = suit
        self.name = card_name
        self.value = value

class Deck():
    def __init__(self):
        self.suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.values = { "Two": 2,
                        "Three": 3,
                        "Four": 4,
                        "Five": 5,
                        "Six": 6,
                        "Seven": 7,
                        "Eight": 8,
                        "Nine": 9,
                        "Ten:" 10,
                        "Jack": 11,
                        "Queen": 12,
                        "King": 13,
                        "Ace": 14 }

        self.deck = [ Card(suit, card_name, self.values[card_name]) for suit in self.suits for card_name in self.values ]
        self.num_cards = len(self.deck)

class Player():
    def __init__(self, number):
        self.number = number
        self.hand = []

    def extend_hand(self, list_cards):
        self.hand = list_cards + self.hand

class War():
    def __init__(self):
        self.player_1 = Player(1)
        self.player_2 = Player(2)

        self.deck = Deck()
        self.all_cards = self.deck.deck
        random.shuffle(self.all_cards)

        self.winner = None
        self.war_condition = False

    def deal_cards(self):
        self.player_1.hand = self.all_cards[:26]
        self.player_2.hand = self.deck[26:]

    def play_war(self):
        self.deal_cards()

        while(True):

            if len(self.player_1.hand) == 0:
                self.winner = 2
            if len(self.player_2.hand) == 0:
                self.winner = 1

            cards_pool = [self.player_1.hand.pop(), self.player_2.hand.pop()]

            if cards_pool[0].value == cards_pool[1].value:
                self.war_condition = True
            elif cards_pool[0].value > cards_pool[1].value:
                self.player_1.extend_hand(cards_pool)
            elif cards_pool[0].value < cards_pool[1].value:
                self.player_2.extend_hand(cards_pool)

            while(self.war_condition):

                player_1_pile = []
                player_2_pile = []

                try:
                    player_1_pile.append(self.player_1.hand.pop()) # face-down card
                    player_1_pile.append(self.player_1.hand.pop()) # face-up card
                    player_2_pile.append(self.player_2.hand.pop()) # face-down card
                    player_2_pile.append(self.player_2.hand.pop()) # face-up card
                except:
                    if len(self.player_1.hand) == 0:
                        self.winner = 2
                        self.war_condition = False
                        break
                    if len(self.player_2.hand) == 0:
                        self.winner = 1
                        self.war_condition = False
                        break
                    break

                if len(self.player_1.hand) == 0:
                    self.winner = 2
                    self.war_condition = False
                    break
                if len(self.player_2.hand) == 0:
                    self.winner = 1
                    self.war_condition = False
                    break

                round_winner = None
                if player_1_pile[-1].value > player_2_pile[-1].value: round_winner = self.player_1
                elif player_1_pile[-1].value > player_2_pile[-1].value: round_winner = self.player_2

                if round_winner:
                    round_winner.extend_hand(cards_pool)
                    round_winner.extend_hand(player_1_pile)
                    round_winner.extend_hand(player_2_pile)

                    self.war_condition = False
                    break

                cards_pool.extend(player_1_pile)
                cards_pool.extend(player_2_pile)

        return self.winner


def play_war():
    war = War()
    winner = war.play_war()

    update_table(winner)

    message = "Winner: Player " + str(winner)
    return message

def lifetime_wins():
    all_results = fetch_history()

    message = "Player " + str(all_results[0][0]) + ": " + str(all_results[0][1]) + " wins"
    message += "Player " + str(all_results[1][0]) + ": " + str(all_results[1][1]) + " wins"

    return message

app.add_url_rule("/play_game", view_func=play_war)
app.add_url_rule("/view_stats", view_func=lifetime_wins)