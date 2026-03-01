import tkinter
from constants import PlayerActions


class PokerGUI:
    def __init__(self, game):
        self.game = game
        self.root = tkinter.Tk()
        self.root.title("AI Poker Coach - Disaster Mode")

        self.title = tkinter.Label(self.root, text="Poker Run", font=("Arial", 18))
        self.title.pack(pady=10)

        self.info = tkinter.Label(self.root, text="", font=("Arial", 12))
        self.info.pack(pady=5)

        self.pot_label = tkinter.Label(self.root, text="", font=("Arial", 12))
        self.pot_label.pack(pady=5)

        self.bet_button = tkinter.Button(self.root, text="Bet",
                                    command=lambda: self.take_action(PlayerActions.BET, 50))
        self.bet_button.pack(pady=5)

        self.check_button = tkinter.Button(self.root, text="Check",
                                      command=lambda: self.take_action(PlayerActions.CHECK))
        self.check_button.pack(pady=5)

        self.fold_button = tkinter.Button(self.root, text="Fold",
                                     command=lambda: self.take_action(PlayerActions.FOLD))
        self.fold_button.pack(pady=5)

        self.update_display()

    def take_action(self, action, amount=0):
        self.game.player_action(action, amount)

        if self.game.is_game_over():
            self.game.on_batch_over()

        self.update_display()

    def update_display(self):
        player = self.game.current_player()
        active_players = [p.name for p in self.game.players if p.active]

        self.info.config(
            text=f"Current Player: {player.name}\n"
                 f"Chips: {player.chips}\n"
                 f"Active Players: {active_players}"
        )

        self.pot_label.config(text=f"Pot: {self.game.pot}")

    def run(self):
        self.root.mainloop()