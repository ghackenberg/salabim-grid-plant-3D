import salabim as sim

from ..model import *
from .robot import *
from .machine import *

class TransversalRobot(Robot):
    def __init__(self, layout: Layout, corridor: Corridor, scenario: Scenario, env: sim.Environment, corridor_stores: list[sim.Store], machine_stores: list[list[sim.Store]], machines: list[SimMachine], x: float, y: float, z: float):
        super().__init__(env, x, y, z, "green")

        self.layout = layout
        self.corridor = corridor
        self.scenario = scenario

        self.corridor_store_main = corridor_stores[0]
        self.corridor_store_left = corridor_stores[1]
        self.corridor_store_right = corridor_stores[2]

        self.machine_stores = machine_stores

        self.machines = machines
