# Entry point for program execution, handles user input and starts simulations todo get up to date
from simulation.game import Game
from simulation.results import Results


def get_samples(number_of_runs, strategy):
    results = Results(strategy)
    for x in range(0, number_of_runs):
        game_won_bool = Game(strategy).run()
        results.add_result(game_won_bool)
    return results