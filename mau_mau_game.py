import logging
import random
from typing import List

import logger.loader
from src import CardDeck, CardGame, CardPlayer

logger = logging.getLogger(__name__)


class MauMauGame:

    # k = Kreuz, p = Pik, h = Herz, c = Karo
    # 7-9, Z = Zehn, B = Bube, D = Dame, K = König, A = Ass
    CARD_LIST = [
        "k7", "k8", "k9", "kZ", "kB", "kD", "kK", "kA",
        "p7", "p8", "p9", "pZ", "pB", "pD", "pK", "pA",
        "h7", "h8", "h9", "hZ", "hB", "hD", "hK", "hA",
        "c7", "c8", "c9", "cZ", "cB", "cD", "cK", "cA",
    ]

    @staticmethod
    def find_card_match(top_card: str, player_hand: List[str]) -> str:
        typ, face = top_card[0], top_card[1]
        fitting_cards = MauMauGame.find_typ_matches(
            player_hand, typ) + MauMauGame.find_face_matches(player_hand, face)
        if len(fitting_cards) == 0:
            raise LookupError('No matching card found...')
        if len(fitting_cards) == 1:
            return fitting_cards[0]
        return MauMauGame.get_random_fitting_card(fitting_cards)

    @staticmethod
    def get_random_fitting_card(fitting_cards):
        random_index = random.randint(0, len(fitting_cards) - 1)
        return fitting_cards[random_index]

    @staticmethod
    def find_face_matches(player_hand, face) -> List[str]:
        return list(filter(lambda card: card[1] == face, player_hand))

    @staticmethod
    def find_typ_matches(player_hand, typ) -> List[str]:
        return list(filter(lambda card: card[0] == typ, player_hand))

    def play(self):
        game = CardGame(
            CardDeck(self.CARD_LIST),
            [CardPlayer("Felix"), CardPlayer("Lena"), CardPlayer("Leonie")],
            6
        )
        print(game)
        current_player = game.get_current_player()
        top_card = game.get_top_card_on_discard_pile()
        logger.info(f"Top Card: {top_card}")
        while not game.is_finished:
            player_cards = current_player.get_cards()
            try:
                logger.debug(f"{current_player.name} has {player_cards}")
                card_to_play = self.find_card_match(top_card, player_cards)
                current_player.play_card(card_to_play)
                game.play_one_card(card_to_play)
                top_card = card_to_play
                logger.info(f"{current_player.name} played {card_to_play}")
                if current_player.get_card_count() == 0:
                    game.set_game_finished()
                    print(f"{current_player.name} has won!")
            except LookupError:
                current_player.add_card(game.draw_one_card())
                logger.info(f"{current_player.name} did draw a card.")

            current_player = game.pass_to_next_player()


if __name__ == '__main__':
    game = MauMauGame()
    game.play()
