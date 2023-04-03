import salabim as sim

from ..model import *
from .robot import *

class TransversalRobot(Robot):
    def __init__(self, layout: Layout, corridor: Corridor, scenario: Scenario, env: sim.Environment, stores: list[sim.Store], x: float, y: float, z: float):
        super().__init__(env, x, y, z, "green")

        self.layout = layout
        self.corridor = corridor
        self.scenario = scenario

        self.store_main = stores[0]
        self.store_left = stores[1]
        self.store_right = stores[2]