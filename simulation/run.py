import sys
from simulation.sample_handler import get_samples
from simulation.game import Game


# todo should i be not providing default values here
def main():
    times_to_run = int(sys.argv[1]) if len(sys.argv) > 1 else 1000
    doors_count = int(sys.argv[2]) if len(sys.argv) > 2 else 3
    open_count = int(sys.argv[3]) if len(sys.argv) > 3 else 1
    if doors_count-2 < open_count:
        open_count = doors_count - 2

    keep = get_samples(times_to_run, doors_count, open_count, Game.Strategy.keep)
    change = get_samples(times_to_run, doors_count, open_count, Game.Strategy.change)

    print(keep)
    print(change)


if __name__ == "__main__":
    main()