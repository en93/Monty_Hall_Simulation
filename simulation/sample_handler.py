# Handles iteration of sampling using the Game class
from simulation.game import Game
from simulation.results import Results


def get_samples(number_of_runs, doors_count, open_count, strategy):
    results = Results(strategy)
    for _ in range(0, number_of_runs):
        outcome = Game(strategy, doors_count, open_count).run()
        results.add_result(outcome)
    return results
