from enum import Enum


class Door:
    def __init__(self):
        self.value = DoorStatus.EMPTY


class DoorStatus(Enum):
    EMPTY = 0
    PRIZE = 1
