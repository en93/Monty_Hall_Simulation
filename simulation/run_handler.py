# Entry point for program execution, handles user input and starts simulations
import sys
from simulation.game import Game


def main():
    wins = 0
    losses = 0
    number_of_runs = get_run_count()
    # todo is there a more elegant way of looping?
    for x in range(0, number_of_runs):
        result = Game(Game.GameStrategy.keep).run()
        if result: #todo bad name there
            wins += 1
        else:
            losses += 1
    print("wins: ", wins, ", losses: ", losses)


def get_run_count():
    if len(sys.argv) > 1:
        num = int(sys.argv[1])
    else:
        num = 3
    return num


if __name__ == "__main__": main()