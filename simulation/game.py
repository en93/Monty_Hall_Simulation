# Represents a single play of the game that is won or lost
import random
from simulation.door import Door, DoorStatus


class Game:
    DOOR_COUNT = 3  # todo make changable

    def __init__(self, strategy):
        self.strategy = strategy

    def run(self):  # todo fix bug always wins
        # Setup doors with randomly placed prize
        # doors_all = [Door()] * self.DOOR_COUNT
        doors_all = []
        i = 0
        while i < self.DOOR_COUNT: #todo do better
            doors_all.append(Door())
            i += 1
        index_of_prize = random.randint(0, self.DOOR_COUNT - 1)
        doors_all[index_of_prize].value = DoorStatus.PRIZE
        index_door_chosen = random.randint(0, self.DOOR_COUNT - 1)

        # Create data structures
        door_chosen = doors_all[index_door_chosen]
        door_prize = doors_all[index_of_prize]
        doors_openable = list(filter(lambda z: z != door_prize and z != door_chosen, doors_all))
        # print(len(doors_closable))

        # Open random door for player, remove door from list
        index_close = random.randint(0, len(doors_openable) - 1)
        doors_openable.pop(index_close)

        # Big reveal
        result = door_chosen == door_prize
        return result

    class GameStrategy:
        change = 0
        keep = 1
