from constants import PlayerActions
from player import Player
from pydealer import Deck, Card

class Game:
    players: list[Player]
    pot: int
    current_deck: Deck
    cards_on_table: list[Card]
    
    
    def __init__(self):
        pass
    
    def play(self):
        for player in self.players:
            player.get_cards()
            
        while not self.is_game_over():
            player = self.get_next_player()
            if player:
                decision, amount = player.make_decision()
                if decision == PlayerActions.FOLD:
                    player.set_active(False) # Player is now inactive
                elif decision == PlayerActions.BET:
                    player.bet(amount)
                    self.pot += amount
                    self.on_raise()
            else:
                self.on_batch_over()
                
    def is_game_over(self) -> bool:
        return True
    
    def on_raise(self) -> None:
        """Call all players' on_raise to see if they match or fold"""
        player = self.get_next_player()
        if player:
            decision, amount = player.make_decision()
            if decision == PlayerActions.FOLD:
                player.set_active(False) # Player is now inactive
            elif decision == PlayerActions.BET:
                player.bet(amount)
                self.pot += amount
            elif decision == PlayerActions.CALL:
                player.bet(amount)
                self.pot += amount
    
    def on_batch_over(self):
        pass
    
    def get_winner(self) -> Player:
        pass
    
    def get_next_player(self) -> Player | None:
        return Player() # todo