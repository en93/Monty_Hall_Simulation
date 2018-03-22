# Used to store outcomes and present the information
class Results:
    def __init__(self, strategy):
        self.strategy = strategy
        self.wins = 0
        self.losses = 0

    def add_result(self, won_game):
        if won_game:
            self.wins += 1
        else:
            self.losses += 1

    def __str__(self):
        return "{}\n\t {}: {}, {}: {}, {}: {}%".format(self.strategy, "Won", self.wins, "Lost", self.losses,
                "Percentage", self.wins/(self.wins+self.losses)*100)

