import pydealer
from random import randint

import player
from deck import Deck
from player import Player

class Game:
    """ obj to make player bet more chips or go all in
        dealers are the same the entire game, blind is to the left of the dealer
        precondition = player on the left indicated by next player in the list
    """
    def __init__(self, player_list):
        self.player_list = player_list
        self.current_player = None
        self.dealer_button = self.current_player
        self.current_bet = None
        self.round_tracker = False
        self.player_status = {}

    def add_player(self, player) -> None:
        self.player_list.append(player)

    def remove_player(self, player) -> None:
        if self.player_list == []:
            raise ValueError("There are no players in the game at the moment")
        else:
            self.player_list.remove(player)

    def player_to_start(self) -> None:
        random_number = randint(0, len(self.player_list) - 1)
        if self.current_player is None:
            self.current_player = self.player_list[random_number]

    def switch_player(self) -> None:
        if self.current_player is None:
            self.current_player = self.current_player.player_to_start()
            player_index = self.player_list.index(self.current_player)
            self.player_list = self.player_list[player_index:] + self.player_list[:player_index-1]
        else:
            first_player = self.player_list.pop(0)
            self.current_player.append(first_player)
            self.current_player = self.player_list[0]

    def player_callin(self, player_call):
        if player_call == "check":
            self.player_list.switch_player()
            for player in self.player_list:
                if self.current_bet > player.amount and player != "folded":
                    difference = self.current_bet - player.amount
                    player.bet(difference)
        elif player_call == ""

    def raise_bet(self, value, player) -> None:
        if self.current_player != "folded":
            current_raise = player.bet(value)
            self.current_bet = current_raise

    def start_round(self):
        self.round_tracker = True

    def end_round(self):
        self.round_tracker = False

    def start_game(self):


    def end_game(self):
        self.