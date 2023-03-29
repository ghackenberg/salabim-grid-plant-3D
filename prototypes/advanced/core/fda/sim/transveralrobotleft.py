import salabim as sim

from ..model import *


class TransversalRobotLeft(sim.Component):
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

    #movements
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

        machine_left_count = len(self.corridor.machinesLeft)

        x_len_left = machine_left_count * 2 + 0.38
        x_left = -0.86 - x_len_left / 2

        while True:
            machine_num = 0
            for machine in self.corridor.machinesLeft:
                x = +3 + machine_num * 2

                # Move down
                print("Move down")
                self.next_z = 1.25
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
                print("Move forward", self.env.now())
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

                # Move Right
                print("Move backward")
                self.next_x = 1
                self.next_t = self.env.now() + duration
                yield self.hold(duration)
                self.x = self.next_x

                machine_num = machine_num + 1