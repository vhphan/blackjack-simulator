from enum import Enum
import random
from collections import namedtuple

Card = namedtuple('Card', ['suit', 'rank'])


# BEGIN: 8d5c7f7d

class Rank(Enum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13


# END: 8d5c7f7d

# BEGIN: 3f3c8f5d
class Suit(Enum):
    HEARTS = 'Hearts'
    DIAMONDS = 'Diamonds'
    CLUBS = 'Clubs'
    SPADES = 'Spades'


# END: 3f3c8f5d

class Deck:

    def __init__(self):
        self.cards = []
        self.reset()

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        if len(self.cards) == 0:
            return None
        return self.cards.pop()

    def make_deck(self):
        return [Card(suit, rank) for suit in Suit for rank in Rank]

    def reset(self):
        self.cards = self.make_deck()

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, index):
        return self.cards[index]


class Multidecks(Deck):
    def __init__(self, num_decks):
        self.cards = []
        self.num_decks = num_decks
        self.reset()

    def reset(self):
        self.cards = []
        for _ in range(self.num_decks):
            self.cards += self.make_deck()
