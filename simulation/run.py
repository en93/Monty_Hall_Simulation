import sys
from simulation.sample_handler import get_samples
from simulation.game import Game


def main():
    times_to_run = sys.argv[1] if len(sys.argv)>=2 else 1000

    keep = get_samples(times_to_run, Game.Strategy.keep)
    change = get_samples(times_to_run, Game.Strategy.change)

    print(keep)
    print(change)


if __name__ == "__main__":
    main()