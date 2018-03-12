# Represents a single play of the game that is won or lost
import random
# from enum import Enum


from simulation.door import Door, DoorStatus


class Game:

    def __init__(self, strategy):
        self.strategy = strategy

    def run(self):

        DOOR_COUNT = 3 #todo make changable

        #Setup doors with randomly placed prize
        doors_all = [Door()] * DOOR_COUNT
        index_of_prize = random.randint(0, DOOR_COUNT-1)
        doors_all[index_of_prize].value = DoorStatus.PRIZE
        index_door_chosen = random.randint(0, DOOR_COUNT - 1)

        #Create data structures
        door_chosen = doors_all[index_door_chosen]
        door_prize = doors_all[index_of_prize]
        doors_empty = filter(lambda x: x.value == DoorStatus.EMPTY, doors_all)

        #Open random door for player, remove door from list


        # if self.strategy



class GameStrategy:
    change = 0
    keep = 1


