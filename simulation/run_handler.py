# Entry point for program execution, handles user input and starts simulations
import sys


def main():
    wins = 0
    losses = 0
    number_of_runs = get_run_count()
    # todo is there a more elegant way of looping?
    for x in range(0, number_of_runs):
        result = Game()
        wins += result[0]
        losses += result[1]
    print(wins, losses)



def get_run_count():
    if len(sys.argv) > 1:
        num = sys.argv[1]
    else:
        num = 3
    return num


if __name__ == "__main__": main()