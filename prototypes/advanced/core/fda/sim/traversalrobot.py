import salabim as sim

from ..model import *
from .robot import *

class TransversalRobot(Robot):
    def __init__(self, layout: Layout, corridor: Corridor, scenario: Scenario, env: sim.Environment, x: float, y: float, z: float):
        super().__init__(env, x, y, z, "green")

        self.layout = layout
        self.corridor = corridor
        self.scenario = scenario