from typing import List

from .error import NotInHandError


class CardPlayer:

    player_count = 0

    def __init__(self, name: str = ""):
        CardPlayer.player_count += 1
        self.name = self._create_player_name(name)
        self.cards = []

    def __del__(self):
        CardPlayer.player_count -= 1

    def __repr__(self):
        return f"{self.name} has {self.cards} in hand."

    def __str__(self):
        return self.__repr__()

    @classmethod
    def with_cards(self, cards: List[str], name: str = "") -> 'CardPlayer':
        player = CardPlayer(name)
        player.add_cards(cards)
        return player

    def _create_player_name(self, name):
        if not name:
            return f"Player{CardPlayer.player_count}"
        return name

    def get_name(self) -> str:
        return self.name

    def get_cards(self) -> List[str]:
        return self.cards

    def get_card_count(self) -> int:
        return len(self.cards)

    def add_cards(self, cards: List[str]):
        self.cards.extend(cards)

    def add_card(self, card: str):
        self.cards.append(card)

    def play_card(self, card: str):
        if card not in self.cards:
            raise NotInHandError(card)
        self.cards.remove(card)
