# Represents a single play of the game that is won or lost
import random
from simulation.door import Door, DoorStatus


class Game:

    DOOR_COUNT = 3

    #Setup doors with randomly placed prize
    doors = [Door()] * DOOR_COUNT
    index_of_prize = random.randint(0, DOOR_COUNT-1)
    doors[index_of_prize].value = DoorStatus.PRIZE #todo is there a more pythonic way that allows encapsulation?

    #Make random choice from range of doors
    index_of_door_chosen = random.randint(0, DOOR_COUNT-1)
    door_chosen = doors[index_of_door_chosen]

    #Open random door for player, remove door from list