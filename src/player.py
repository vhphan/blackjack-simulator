from src.hand import BlackjackHand


class Player:
    from deck import BlackjackHand

    class Player:
        def __init__(self, name, chips):
            self.name = name
            self.chips = chips
            self.hand = BlackjackHand()

    def bet(self, amount):
        if amount > self.chips:
            raise ValueError("Bet amount exceeds chips")
        self.chips -= amount
        return amount
