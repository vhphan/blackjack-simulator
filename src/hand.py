from src.deck import Card, Rank


class BlackjackHand:
    def __init__(self):
        self.cards = []
        self._value = 0

    def add_card(self, card):
        if not isinstance(card, Card):
            raise TypeError("Invalid card object")
        self.cards.append(card)
        if len(self.cards) >= 2:
            self._value = self.get_value()

    def remove_card(self):
        if len(self.cards) == 0:
            return None
        return self.cards.pop()

    def get_value(self):
        value = 0
        num_aces = 0
        for card in self.cards:
            if card.rank == Rank.ACE:
                num_aces += 1
                continue
            elif card.rank in [Rank.JACK, Rank.QUEEN, Rank.KING]:
                value += 10
            else:
                print(f'card.rank: {card.rank} is of type {type(card.rank)}')
                print(f'value is {value} and is of type {type(value)}')
                value += card.rank.value

        for _ in range(num_aces):
            if value + 11 <= 21:
                value += 11
            else:
                value += 1

        return value

    def is_bust(self):
        return self._value > 21

    def is_blackjack(self):
        return len(self.cards) == 2 and self._value == 21

    def __str__(self):
        return ", ".join(f"{card.rank}{card.suit[0]}" for card in self.cards)

    def __len__(self):
        return len(self.cards)
