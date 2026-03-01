from player import Player


class Ledger:
    def __init__(self):
        self.player_list = []
        self.ledger = {}

    def add_player(self, player):
        self.ledger[player] = {"balance": 0, "score": 0, "locked": False}
        self.player_list.append(player)

    def update_balance(self, player, amount):
        if self.ledger[player]["locked"]:
            raise ValueError(f"{player.name} is locked out.")

        self.ledger[player]["balance"] += amount

        if self.ledger[player]["balance"] < 0:
            self.ledger[player]["locked"] = True

    def update_score(self, player, points):
        self.ledger[player]["score"] += points

    def unlock_all(self):
        for player in self.player_list:
            self.ledger[player]["locked"] = False

    def print_ledger(self):
        for player in self.player_list:
            data = self.ledger[player]
            print(player.name, "Balance:", data["balance"],
                  "Score:", data["score"], "Locked:", data["locked"])

