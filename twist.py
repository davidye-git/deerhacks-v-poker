#a game affected by a twist, that can either be natural disaster with different degrees of damage to the game
#or dealer leaving the game all of a sudden or game changes with mafia
import pydealer

class NaturalDisaster:
    """ Natural Disaster occurs which shuffles their decks, cause mayhem, damage banks and pots"""
    weather_condition: str
    bank: float
    def __init__(self, weather_conditions, bank):
        self.weather_conditions = weather_conditions
        self.bank = bank

    def sudden_storm(self, storm):
        self.weather_conditions = storm

    def attack_on_casino(self):

class DealerRun:


class ChangeGame:

