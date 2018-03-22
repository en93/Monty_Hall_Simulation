# Model used to represent a door
from enum import Enum, auto


class Door:
    def __init__(self):
        self.value = Door.DoorStatus.EMPTY

    class DoorStatus(Enum):
        EMPTY = auto()
        PRIZE = auto()
