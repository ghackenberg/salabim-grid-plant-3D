import salabim as sim

from ..model import *
from .traversalrobot import *


class TransversalRobotRight(TransversalRobot):
    def __init__(self, corridor: Corridor, env: sim.Environment, x: float, y: float, z: float):
        super().__init__(corridor, env, x, y, z)

    def process(self):
        duration = 1

        while True:
            machine_num = 0
            for machine in self.corridor.machinesRight:
                x = -3 - machine_num * 2

                # Move down
                yield from self.move_z(1.25, duration)
                # Move up
                yield from self.move_z(2.5, duration)
                # Move Right
                yield from self.move_x(x, duration)
                # Move down
                yield from self.move_z(1.5, duration)
                # Move up
                yield from self.move_z(2.5, duration)
                # Move Left
                yield from self.move_x(-1, duration)

                machine_num = machine_num + 1