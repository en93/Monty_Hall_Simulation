from simulation.game_outcome import Outcome

# Used to store outcomes and present the information
class Results:
    def __init__(self, strategy):
        self.strategy = strategy
        self.wins = 0
        self.losses = 0

    def add_result(self, result):
        if result == Outcome.WON:
            self.wins += 1
        elif result == Outcome.LOST:
            self.losses += 1

    def __str__(self):
        return "{}\n\t {}: {}, {}: {}, {}: {}%".format(self.strategy, "Won", self.wins, "Lost", self.losses,
                "Percentage won", self.wins/(self.wins+self.losses)*100)

