import salabim as sim

from ..model import *
from .arm import *

class SimCorridor(sim.Component):
    def __init__(self, corridor: Corridor, env: sim.Environment, y: float):
        super().__init__()

        # CORRIDOR
        self.corridor = corridor

        # MACHINES
        machines_left = corridor.machines_left
        machines_right = corridor.machines_right

        # ENVIRONMENT
        self.env = env

        # STORE
        store_main = sim.Store(f"Corridor {corridor.code} main")
        store_left = sim.Store(f"Corridor {corridor.code} left")
        store_right = sim.Store(f"Corridor {corridor.code} right")

        # SIM ARMS
        self.sim_arm_left = SimArm(corridor, machines_left, "left", env, store_left, store_right, store_main, +1, y)
        self.sim_arm_right = SimArm(corridor, machines_right, "right", env, store_right, store_left, store_main, -1, y)

        # VERTICAL BOX
        sim.Animate3dBox(x_len=0.25, y_len=0.25, z_len=1.5, color="red", x=0, y=y, z=1.625)

        # STORAGE BOX
        sim.Animate3dBox(x_len=3, y_len=1, z_len=1, color='orange', x=0, y=y, z=0.5)
    
    def printStatistics(self):
        print(f"Corridor {self.corridor.code}:")
        self.sim_arm_left.printStatistics()
        self.sim_arm_right.printStatistics()
    