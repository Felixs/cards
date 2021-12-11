import os
from collections import deque
from typing import List

from . import CardDeck, CardPlayer, DiscardPile
from .error import NoPlayersError, OutOfCardsError


class CardGame:

    def __init__(self, card_deck: CardDeck, players: List[CardPlayer], init_card_draw: int):
        self.deck = card_deck
        self.deck.shuffle()
        self.players = self._create_player_quere(players)
        self._draw_initial_cards(init_card_draw)
        self.discard_pile = DiscardPile()
        self.discard_pile.add_card(self.deck.draw())
        self.is_finished = False

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"{os.linesep.join([str(player) for player in self.players])}{os.linesep}{self.deck.remainig_number_of_cards()} cards remain in the deck"

    @classmethod
    def with_unnamed_players(cls, card_deck: CardDeck, num_of_players: int, init_card_draw: int) -> 'CardGame':
        players = [CardPlayer() for _ in range(num_of_players)]
        return CardGame(card_deck, players, init_card_draw)

    def _create_player_quere(self, players: List[CardPlayer]):
        if len(players) == 0:
            raise NoPlayersError("No players want to play :(")
        return deque(players)

    def _draw_initial_cards(self, init_card_draw):
        for _ in range(init_card_draw):
            for player in self.players:
                player.add_card(self.deck.draw())

    def get_current_player(self) -> CardPlayer:
        return self.players[0]

    def pass_to_next_player(self) -> CardPlayer:
        self.players.rotate(-1)
        return self.get_current_player()

    def get_top_card_on_discard_pile(self) -> str:
        return self.discard_pile.get_top_card()

    def draw_one_card(self) -> str:
        if self.deck.is_depleted():
            self._shuffle_discard_into_deck()
        return self.deck.draw()

    def play_one_card(self, card: str):
        self.discard_pile.add_card(card)

    def set_game_finished(self):
        self.is_finished = True

    def _shuffle_discard_into_deck(self):
        discared_cards = self.discard_pile.empty(keep_top_card=True)
        if len(discared_cards) == 0:
            raise OutOfCardsError(
                "No cards in discard pile to shuffle back into deck!")
        self.deck.add_cards(discared_cards)
        self.deck.shuffle()
