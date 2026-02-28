import pydealer

class Player:
    """
    A regular player in a poker game.
    """
    player_name: str
    hand: list[pydealer.Card]

    def __init__(self, player_name: str) -> None:
        """
        Initialize this player.

        Precondition: len(player_name) > 0
        """
        self.player_name = player_name
        self.hand = []
        self.cash = 1000
        self.bet_amount = 0
        self.status = "playing"

    def __str__(self) -> str:
        return (f"Player {self.player_name} has status {self.status} and cash "
                f"{self.cash}")

    def change_status(self, status: str) -> None:
        """
        Change <self.status> for the current turn.

        Precondition: <status> is either "playing", or "folded".
        """
        self.status = status

    def bet(self, amount: int) -> int:
        self.bet_amount = amount
        self.cash -= amount
        return amount

    def new_round(self) -> None:
        self.hand = []
        self.bet_amount = 0
        self.change_status("playing")

class MrCasino(Player):
    """
    The overpowered bot poker player.
    """
    def __init__(self) -> None:
        super().__init__("Mr. Casino")
