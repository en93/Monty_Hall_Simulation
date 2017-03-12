import random
import sys


class Cases:
    keep_door = 1
    change_door = 2


class DoorsList:
    def __init__(self):
        self.door_values = [0, 0, 0]
        self.correct_door = random.randrange(0, 3)
        self.door_values[self.correct_door] = 1
        self.chosen_door = None

    def choose_door(self, index):
        self.chosen_door = index

    def close_door(self):
        empty_door = self.door_values.index(0)
        if empty_door == self.chosen_door:
            empty_door = len(self.door_values) - 1 - self.door_values[::-1].index(0)
        self.door_values[empty_door] = -1  # -1 indicate the door is closed

    def change_door_chosen(self):
        if self.door_values[self.chosen_door] == 1:
            self.chosen_door = self.door_values.index(0)
        elif self.door_values[self.chosen_door] == 0:
            self.chosen_door = self.door_values.index(1)

    def is_correct_door_chosen(self):
        if self.chosen_door == self.correct_door:
            return True
        else:
            return False


def simulate_monty_hall(case):
    doors = DoorsList()
    player_chosen_door = random.randrange(0, 3)
    doors.choose_door(player_chosen_door)
    doors.close_door()
    if case == Cases.change_door:  # When we want to change doors
        doors.change_door_chosen()
    if doors.is_correct_door_chosen():
        return 1
    else:
        return 0


def get_number_of_runs():
    if len(sys.argv) > 1:
        try:
            test_runs = int(float(sys.argv[1]))
            if test_runs < 1:
                print("Invalid input, please enter a number of at least one")
                exit()
        except ValueError:
            print("Invalid input, please enter a number")
            exit()
    else:
        test_runs = 1000
    return test_runs


def run_simulations(case, test_runs):
    i = 0
    win_count = 0
    while i < test_runs:
        win_count += simulate_monty_hall(case)
        i += 1
    return win_count


def main():
    test_runs = get_number_of_runs()
    keep_door_count = run_simulations(Cases.keep_door, test_runs)
    change_door_count = run_simulations(Cases.change_door, test_runs)
    print("Not changing doors: \nGives {} wins out of {} games\n".format(keep_door_count, test_runs))
    print("Changing doors: \nGives {} wins out of {} games\n".format(change_door_count, test_runs))


if __name__ == "__main__": main()
