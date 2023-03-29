import salabim as sim

from ..model import *


class TransversalRobotRight(sim.Component):
    def __init__(self, corridor: Corridor, env: sim.Environment, x: float, y: float, z: float):
        super().__init__()

        self.corridor = corridor
        self.env = env

        self.x = x
        self.y = y
        self.z = z
        self.t = env.now()

        self.next_x = x
        self.next_z = z
        self.next_t = env.now()

        sim.Animate3dBox(x_len=0.5, y_len=0.5, z_len=0.5, color="green", edge_color='white', x=self.x_func, y=self.y, z=self.z_func)
    
    def x_func(self, t: float):
        if self.next_t == self.t:
            return self.x
        else:
            return self.x + (self.next_x - self.x) * (t - self.t) / (self.next_t - self.t)

    def z_func(self, t: float):
        if self.next_t == self.t:
            return self.z
        else:
            return self.z + (self.next_z - self.z) * (t - self.t) / (self.next_t - self.t)

    def process(self):
        duration = 1

        while True:
            machine_num = 0
            for machine in self.corridor.machinesRight:
                x = -3 - machine_num * 2

                # Move down
                self.next_z = 1.25
                self.next_t = self.env.now() + duration
                yield self.hold(duration)
                self.z = self.next_z

                # Move up
                self.next_z = 2.5
                self.next_t = self.env.now() + duration
                yield self.hold(duration)
                self.z = self.next_z

                # Move Right
                self.next_x = x
                self.next_t = self.env.now() + duration
                yield self.hold(duration)
                self.x = self.next_x

                # Move down
                print("Move down")
                self.next_z = 1.5
                self.next_t = self.env.now() + duration
                yield self.hold(duration)
                self.z = self.next_z

                # Move up
                print("Move up")
                self.next_z = 2.5
                self.next_t = self.env.now() + duration
                yield self.hold(duration)
                self.z = self.next_z

                # Move Left
                self.next_x = -1
                self.next_t = self.env.now() + duration
                yield self.hold(duration)
                self.x = self.next_x

                machine_num = machine_num + 1