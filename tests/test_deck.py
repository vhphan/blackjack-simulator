from src.deck import Deck
from src.hand import BlackjackHand
from src.deck import Card
from src.deck import Multidecks

def test_make_deck():
    deck = Deck()
    result = deck.make_deck()
    assert len(result) == 52
    assert all(isinstance(card, Card) for card in result)

# Check if the shuffle method randomizes the order of cards in the deck
def test_shuffle_deck():
    deck = Deck()
    initial_order = list(deck)
    deck.shuffle()
    assert list(deck) != initial_order

# Adds cards to the deck based on the number of decks specified
def test_add_cards_to_deck():
    deck = Multidecks(3)
    deck.reset()
    assert len(deck.cards) == 156


# Check if the shuffle method randomizes the order of cards in the deck
def test_shuffle_deck():
    deck = Deck()
    initial_order = list(deck)
    deck.shuffle()
    assert list(deck) != initial_order


# Check if the deck is empty after dealing all cards
def test_deck_empty_after_dealing_all_cards():
    deck = Deck()
    for _ in range(52):
        deck.draw_card()
    assert len(deck) == 0

# Check if dealing a card returns a Card instance
def test_draw_card_returns_card_instance():
    deck = Deck()
    card = deck.draw_card()
    assert isinstance(card, Card)

# Check if shuffling the deck maintains the number of cards
def test_shuffle_deck_maintains_card_count():
    deck = Deck()
    initial_count = len(deck)
    deck.shuffle()
    assert len(deck) == initial_count

# Check if resetting a Multidecks instance returns it to the initial state
def test_multidecks_reset_returns_to_initial_state():
    deck = Multidecks(3)
    deck.shuffle()
    deck.draw_card()
    deck.reset()
    assert len(deck) == 156
    assert all(isinstance(card, Card) for card in deck.cards)

