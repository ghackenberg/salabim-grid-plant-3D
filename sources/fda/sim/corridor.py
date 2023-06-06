import salabim as sim

from ..model import Corridor

from .arm import SimArm


class SimCorridor(sim.Component):
    def __init__(self, corridor: Corridor, env: sim.Environment, y: float):
        super().__init__()

        self.corridor = corridor

        self.env = env

        # Machines
        machines_left = corridor.machines_left
        machines_right = corridor.machines_right

        # Corridor stores
        store_main = sim.Store(f"Store main")
        store_left = sim.Store(f"Store left")
        store_right = sim.Store(f"Store right")

        self.store_main = store_main
        self.store_left = store_left
        self.store_right = store_right

        # Left and right arms
        self.sim_arm_left = SimArm(corridor, machines_left, "left", env, store_left, store_right, store_main, +1, y)
        self.sim_arm_right = SimArm(corridor, machines_right, "right", env, store_right, store_left, store_main, -1, y)

        # Corridor storage vertical box
        sim.Animate3dBox(x_len=0.25, y_len=0.25, z_len=1.5, color="red", x=0, y=y, z=1.625)

        # Corridor storage box
        sim.Animate3dBox(x_len=3, y_len=1, z_len=1, color='orange', x=0, y=y, z=0.5)
    
    def printStatistics(self):
        print(f" - {self.corridor.name}:")
        self.sim_arm_left.printStatistics()
        self.sim_arm_right.printStatistics()
    
    def utilization(self):
        left_len = len(self.sim_arm_left.sim_machines)
        right_len = len(self.sim_arm_right.sim_machines)
        left = self.sim_arm_left.utilization()
        right = self.sim_arm_right.utilization()
        if left_len > 0 and right_len > 0:
            return (left * left_len + right * right_len) / (left_len + right_len)
        elif left_len > 0:
            return left
        elif right_len > 0:
            return right
        else:
            return 1
    
    def plot(self):
        pass
    