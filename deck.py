import pydealer
from player import Player

class Deck:
    deck: pydealer.Deck
    playing_field: list[str]
    pot: int

    def __init__(self) -> None:
        self.deck = pydealer.Deck()
        self.playing_field = []
        self.discard_pile = []
        self.pot = 0

    def shuffle(self):
        self.deck.shuffle()

    def draw_to_players(self, players: list[Player]) -> None:
        for player in players:
            player.hand.append(self.deck.deal(2))

    def draw_cards(self) -> None:
        if len(self.playing_field) == 0:
            self.discard_pile.append(self.deck.deal(1))
            self.playing_field.append(self.deck.deal(3))

        self.discard_pile.append(self.deck.deal(1))
        self.playing_field.append(self.deck.deal(1))

    def blinds(self, players: list[Player], blind: int) -> None:
        self.pot += blind
        for i in range(len(players) - 1):
            self.pot += players[i].bet(blind)

    def bet_chips(self, players: list[Player]) -> None:
        for player in players:
            self.pot += player.bet()

    def reset_deck(self) -> None:
        self.deck = pydealer.Deck()
        self.playing_field = []
        self.pot = 0

# deck = Deck()
# deck.shuffle()
# deck.draw_cards()
# print(deck.playing_field)
# deck.draw_cards()
# print(deck.playing_field)
# deck.draw_cards()
# print(deck.playing_field)
