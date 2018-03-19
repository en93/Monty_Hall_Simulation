# Represents a single play of the game that is won or lost
import random
from simulation.door import Door, DoorStatus


class Game:
    DOOR_COUNT = 3  # todo make changable

    def __init__(self, strategy):
        self.strategy = strategy
        self.doors_all = []
        self.door_chosen = None
        self.door_prize = None
        self.doors_can_open = None

    def run(self):  # todo fix bug always wins
        self.setup_doors()


        # Open random door for player, remove door from list, only needed if multiple iterations
        index_close = random.randint(0, len(doors_openable) - 1)
        doors_openable.pop(index_close) #todo this is bad, still in other data structures, create list of what i can use

        #If changing doors do so

        # Big reveal
        result = door_chosen == door_prize
        return result

    def setup_doors(self):
        self.doors_all = Game.make_doors()
        self.door_prize = Game.place_prize(self.doors_all)
        self.door_chosen = Game.choose_door(self.doors_all)
        self.doors_can_open = list(filter(lambda z: z != self.door_prize and z != self.door_chosen, self.doors_all))

    @staticmethod
    def make_doors(self):
        doors = []
        i = 0
        while i < self.DOOR_COUNT:  # todo do better
            doors.append(Door())
            i += 1
        return doors

    @staticmethod
    def place_prize(door_list):
        index_of_prize = random.randint(0, len(door_list) - 1)
        door = door_list[index_of_prize]
        door.value = DoorStatus.PRIZE
        return door

    @staticmethod
    def choose_door(door_list):
        index_door_chosen = random.randint(0, len(door_list) - 1)
        door = door_list[index_door_chosen]
        return door

    class GameStrategy:
        change = 0
        keep = 1
