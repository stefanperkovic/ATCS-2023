"""
A class representing a deck of cards
"""

import random
# TODO 1: Get the card class
from card import Card

class Deck:
    # TODO 2: Constructor Parameters
    def __init__(self, suits=["heart", "club", "diamond", "spade"], ranks=["A", "1", "2" ,"3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]):
        self.cards = []
        
        # Initialize all cards
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        # Pop and return the end card
        if not self.is_empty():
            return self.cards.pop()
        else:
            return None

    # TODO 3: Is the deck empty
    def is_empty(self):
        if len(self.cards) == 0:
            return True
        return False
