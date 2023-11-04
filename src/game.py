from deck import Deck
from hand import BlackjackHand


class BlackjackGame:
    def __init__(self):
        self.deck = Deck()
        self.player_hand = BlackjackHand()
        self.dealer_hand = BlackjackHand()

    def deal_initial_hands(self):
        self.deck.shuffle()
        self.player_hand.add_card(self.deck.draw_card())
        self.dealer_hand.add_card(self.deck.draw_card())
        self.player_hand.add_card(self.deck.draw_card())
        self.dealer_hand.add_card(self.deck.draw_card())

    def player_hits(self):
        self.player_hand.add_card(self.deck.draw_card())

    def dealer_hits(self):
        self.dealer_hand.add_card(self.deck.draw_card())

    def player_bust(self):
        return self.player_hand.is_bust()

    def dealer_bust(self):
        return self.dealer_hand.is_bust()

    def play(self):
        self.deal_initial_hands()
