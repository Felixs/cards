from typing import List

from .error import OutOfCardsError


class DiscardPile:

    def __init__(self):
        self.cards: List[str] = []

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"DiscardPile in order top to bottom: {reversed(self.card_list)}."

    def add_card(self, card: str):
        self.cards.append(card)

    def remove_to_card(self) -> str:
        if self.is_empty():
            raise OutOfCardsError("No cards in discard pile!")
        return self.cards.pop()

    def is_empty(self) -> bool:
        return len(self.cards) == 0

    def empty(self, keep_top_card: bool = False) -> List[str]:
        cards_in_pile = self.cards.copy()
        self.cards.clear()
        if keep_top_card:
            self.cards.append(cards_in_pile.pop())

        return cards_in_pile

    def get_top_card(self) -> str:
        if len(self.cards) == 0:
            raise OutOfCardsError("No cards in discard pile!")

        return self.cards[len(self.cards) - 1]
