from player import Player


class Ledger:
    def __init__(self):
        self.player_list = []
        self.ledger = {}

    def add_player(self, player) -> None:
        self.ledger[player] = {"balance": 0, "score": 0, "locked": False}
        self.player_list.append(player)

    def update_balance(self, player, amount) -> None:
        if self.ledger[player]["locked"]:
            raise ValueError(f"{player.name} is locked out.")

        self.ledger[player]["balance"] += amount

        if self.ledger[player]["balance"] < 0:
            self.ledger[player]["locked"] = True

    def update_score(self, player, points) -> None:
        self.ledger[player]["score"] += points

    def unlock_all(self) -> None:
        for player in self.player_list:
            self.ledger[player]["locked"] = False

    def print_ledger(self) -> None:
        for player in self.player_list:
            data = self.ledger[player]
            print(player.name, "Balance:", data["balance"],
                  "Score:", data["score"], "Locked:", data["locked"])

    def get_highest_balance_player(self) -> Player:
        highest = 0
        for player in self.player_list:
            if self.ledger[player]["balance"] > highest:
                highest = self.ledger[player]["balance"]
                person = player
        return person
