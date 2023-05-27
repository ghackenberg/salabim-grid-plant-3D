import salabim as sim

from ..model import *
from .arm import *

class SimCorridor(sim.Component):
    def __init__(self, corridor: Corridor, env: sim.Environment, y: float):
        super().__init__()

        # CORRIDOR
        self.corridor = corridor

        # ENVIRONMENT
        self.env = env

        # STORE
        self.store_main = sim.Store(f"Corridor {corridor.code} main")
        self.store_left = sim.Store(f"Corridor {corridor.code} left")
        self.store_right = sim.Store(f"Corridor {corridor.code} right")

        # SIM ARMS
        self.sim_arm_left = SimArm(corridor, corridor.machines_left, "left", env, self.store_left, self.store_right, self.store_main, +1, y)
        self.sim_arm_right = SimArm(corridor, corridor.machines_right, "right", env, self.store_right, self.store_left, self.store_main, -1, y)

        # VERTICAL BOX
        sim.Animate3dBox(x_len=0.25, y_len=0.25, z_len=1.5, color="red", x=0, y=y, z=1.625)

        # STORAGE BOX
        sim.Animate3dBox(x_len=3, y_len=1, z_len=1, color='orange', x=0, y=y, z=0.5)
    
    def printStatistics(self):
        print(f"Corridor {self.corridor.code}:")
        self.sim_arm_left.printStatistics()
        self.sim_arm_right.printStatistics()
    