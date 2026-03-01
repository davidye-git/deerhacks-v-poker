from constants import PlayerActions, OnRaiseActions
from pydealer import Deck, Card

class Player:
    active: bool = True
    chips: int = 100
    total_bet: int = 0
    hand = None

    def __init__(self):
        pass
    
    def make_decision(self) -> tuple[PlayerActions, float | None]:
        return PlayerActions.FOLD
    
    def on_raise(self) -> OnRaiseActions:
        return OnRaiseActions.MATCH
    
    def __evaluate_hand(self):
        pass
    
    def get_cards(self, cards: list[any]) -> None:
        self.hand = cards
    
    def set_active(self, active: bool) -> None:
        self.active = active

    def bet(self, amount: int) -> None:
        self.chips -= amount
        self.total_bet += amount
        
    def reset(self) -> None:
        self.active = True
        self.total_bet = 0
        self.hand = None