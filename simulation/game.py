# Represents a single play of the game that is won or lost
import random
from simulation.door import Door, DoorStatus


class Game:
    def __init__(self, strategy):
        self.strategy = strategy
        self.doors_all = []
        self.door_chosen = None
        self.door_prize = None
        self.door_chosen_previous = None

    def run(self):
        self.setup_doors()
        self.choose_door()
        if self.strategy == Game.Strategy.change:
            self.open_empty_door()
            self.choose_door()
        return self.test_win_conditions()

    def setup_doors(self):
        self.doors_all = Game.make_doors(3)
        self.door_prize = Game.place_prize(self.doors_all)

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
        i = 0
        while i < count:
            doors.append(Door())
            i += 1
        return doors

    @staticmethod
    def place_prize(door_list):
        index_of_prize = random.randint(0, len(door_list) - 1)
        door = door_list[index_of_prize]
        door.value = DoorStatus.PRIZE
        return door

    class Strategy:
        change = 0
        keep = 1
