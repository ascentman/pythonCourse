import random

class Card(object):
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def value(self):
        return 0

    def is_joker(self):
        return False


class Deck(object):
    def __init__(self):
        self.cards = []

    def draw(self):
        return self.cards.pop()

    def shuffle(self):
        random.shuffle(self.cards)

    def add(self, card):
        self.cards.append(card)

    def is_empty(self):
        return not len(self.cards)