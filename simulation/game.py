# Represents a single play of the game that is won or lost
import random
from enum import Enum, auto
from simulation.door import Door, DoorStatus


class Game:
    def __init__(self, strategy, doors_count=3, open_count=1):
        self.strategy = strategy
        self.doors_count = doors_count
        self.open_count = open_count
        self.doors_all = []
        self.door_chosen = None
        self.door_prize = None
        self.door_chosen_previous = None

    def run(self):
        self.setup_doors()
        self.choose_door()
        # Note the process of opening doors still occurs in the keep scenario.
        # This was skipped as an optimization as it had no bearing on the outcome
        if self.strategy == Game.Strategy.change:
            for x in range(self.open_count):
                self.open_empty_door()
                self.choose_door()
        return self.test_win_conditions()

    def setup_doors(self):
        self.doors_all = Game.make_doors(self.doors_count)
        self.door_prize = Game.place_prize(self.doors_all)

    # Note that a door can be chosen again later as the script only the most recent door
    def choose_door(self):
        self.door_chosen_previous = self.door_chosen
        doors_can_choose = list(filter(lambda z: z != self.door_chosen_previous, self.doors_all))
        index_door_chosen = random.randint(0, len(doors_can_choose) - 1)
        self.door_chosen = doors_can_choose[index_door_chosen]

    def open_empty_door(self):
        doors_can_open = list(filter(lambda z: z != self.door_prize and z != self.door_chosen, self.doors_all))
        index_close = random.randint(0, len(doors_can_open) - 1)
        door = doors_can_open[index_close]
        self.doors_all.remove(door)

    def test_win_conditions(self):
        result = self.door_chosen == self.door_prize
        return result

    @staticmethod
    def make_doors(count):
        doors = []
        for x in range(count):
            doors.append(Door())
        return doors

    @staticmethod
    def place_prize(door_list):
        index_of_prize = random.randint(0, len(door_list) - 1)
        door = door_list[index_of_prize]
        door.value = DoorStatus.PRIZE
        return door

    class Strategy(Enum):
        change = auto()
        keep = auto()
