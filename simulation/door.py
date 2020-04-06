# Model used to represent a door
from simulation.door_status import DoorStatus


class Door:
    def __init__(self):
        #Set initial value
        self.value = DoorStatus.EMPTY