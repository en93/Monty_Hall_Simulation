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
        return "%s\n\t %s: %d, %s: %d, %s: %s" % (self.strategy, "Won", self.wins, "Lost", self.losses, "Percentage", self.wins/(self.wins+self.losses)*100)
    