
# Generated by CodiumAI
from src.hand import BlackjackHand
from src.deck import Card, Suit, Rank


import pytest

from src.deck import BlackjackHand
from src.deck import Card, Suit, Rank

import pytest

class TestBlackjackHand:

    # Adding cards to the hand updates its value correctly
    def test_adding_cards_updates_value(self):
        hand = BlackjackHand()
        card1 = Card(Suit.SPADES, Rank.ACE)
        card2 = Card(Suit.HEARTS, Rank.KING)
        hand.add_card(card1)
        hand.add_card(card2)
        assert hand.get_value() == 21


    # Removing a card from the hand updates its value correctly
    def test_removing_card_updates_value(self):
        hand = BlackjackHand()
        card1 = Card(Suit.SPADES, Rank.ACE)
        card2 = Card(Suit.HEARTS, Rank.KING)
        hand.add_card(card1)
        hand.add_card(card2)
        hand.remove_card()
        assert hand.get_value() == 11

    # Hand value is correctly calculated with aces
    def test_hand_value_with_aces(self):
        hand = BlackjackHand()
        card1 = Card(Suit.SPADES, Rank.ACE)
        card2 = Card(Suit.HEARTS, Rank.FIVE)
        hand.add_card(card1)
        hand.add_card(card2)
        assert hand.get_value() == 16

    # Adding an invalid card raises a TypeError
    def test_adding_invalid_card_raises_type_error(self):
        hand = BlackjackHand()
        invalid_card = "invalid"
        with pytest.raises(TypeError):
            hand.add_card(invalid_card)

    # Removing a card from an empty hand returns None
    def test_removing_card_from_empty_hand_returns_none(self):
        hand = BlackjackHand()
        assert hand.remove_card() == None

    # Hand value is correctly calculated with multiple aces
    def test_hand_value_with_multiple_aces(self):
        hand = BlackjackHand()
        card1 = Card(Suit.SPADES, Rank.ACE)
        card2 = Card(Suit.HEARTS, Rank.ACE)
        card3 = Card(Suit.DIAMONDS, Rank.FIVE)
        hand.add_card(card1)
        hand.add_card(card2)
        hand.add_card(card3)
        assert hand.get_value() == 17