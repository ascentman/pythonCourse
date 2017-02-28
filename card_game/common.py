# -*- coding: utf-8 -*-
import random

CLUBS = 1
DIAMONDS = 2
HEARTS = 3
SPADES = 4
SUITS = (CLUBS, DIAMONDS, HEARTS, SPADES)
SUITS_SYMBOLS = {
        CLUBS: "♣",
        DIAMONDS: "♦",
        HEARTS: "♥",
        SPADES: "♠",
        }

JACK = 11
QUEEN = 12
KING = 13
ACE = 14
RANKS = (JACK, QUEEN, KING, ACE)
RANKS_SYMBOLS = {
        JACK: 'J',
        QUEEN: 'Q',
        KING: 'K',
        ACE: 'A',
        }


class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def value(self):
        return self.rank

    def is_trump(self):
        return False

    def __str__(self):
        return '%s %s' % (SUITS_SYMBOLS[self.suit], RANKS_SYMBOLS.get(self.rank, self.rank))



class Deck():
    def __init__(self):
        self.cards = []
        super().__init__()
        for suit in SUITS:
            for rank in RANKS:
                self.add(self.create_card(suit, rank))
            for i in range(6,11):
                self.add(self.create_card(suit, i))

    def create_card(self, suit, rank):
        return Card(suit, rank)

    #def draw(self):
    #    return self.cards.pop()

    #def shuffle(self):
    #    random.shuffle(self.cards)

    def add(self, card):
        self.cards.append(card)

    def print_cards(self):
        for c in self.cards:
            print(c)


k = Deck()
k.print_cards()