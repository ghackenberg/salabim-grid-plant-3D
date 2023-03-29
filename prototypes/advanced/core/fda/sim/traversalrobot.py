import salabim as sim

from ..model import *
from .robot import *

class TransversalRobot(Robot):
    def __init__(self, corridor: Corridor, env: sim.Environment, x: float, y: float, z: float):
        super().__init__(env, x, y, z, "green")

        self.corridor = corridor