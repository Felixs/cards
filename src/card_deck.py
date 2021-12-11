import random
from typing import List

from .error import OutOfCardsError


class CardDeck:

    def __init__(self, card_list: List[str]):
        self.cards = card_list.copy()
        self.times_shuffled = 0

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"CardDeck in order top to bottom: {reversed(self.cards)}, shuffeled: {self.times_shuffled} times."

    def shuffle(self):
        random.shuffle(self.cards)
        self.times_shuffled += 1

    def draw(self) -> str:
        if self.is_depleted():
            raise OutOfCardsError(
                "Trying to draw card from an empty card deck!")

        return self.cards.pop()

    def add_cards(self, cards: List[str]):
        self.cards.extend(cards)

    def remainig_number_of_cards(self) -> int:
        return len(self.cards)

    def is_depleted(self) -> bool:
        return len(self.cards) == 0
