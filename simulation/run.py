# Script is used to gather sample data, expects command line input
import sys
from simulation.sample_handler import get_samples
from simulation.game import Game
from simulation.strategy import Strategy

def main():
    #Set default params
    sample_size = 1000
    num_doors = 3
    num_opens = 1

    #Read command line args if present
    if len(sys.argv) >= 2:
        sample_size = int(sys.argv[1])
    if len(sys.argv) >= 3:
        num_doors = int(sys.argv[2])
    if len(sys.argv) >= 4:
        num_opens = int(sys.argv[3])
        #Ensure there are at least two doors left at the end
        if num_doors-2 < num_opens:
            num_opens = num_doors - 2

    keep = get_samples(sample_size, num_doors, num_opens, Strategy.keep)
    change = get_samples(sample_size, num_doors, num_opens, Strategy.change)

    print(keep)
    print(change)

#Call main method when called from command line
if __name__ == "__main__":
    main()