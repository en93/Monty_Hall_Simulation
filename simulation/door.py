from enum import Enum, auto

class Door:
    def __init__(self):
        self.value = DoorStatus.EMPTY


class DoorStatus(Enum):
    EMPTY = auto()
    PRIZE = auto()

    #todo move set getter func to this class
