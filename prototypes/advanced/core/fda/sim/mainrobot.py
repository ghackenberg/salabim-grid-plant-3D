import salabim as sim

from ..model import *


class MainRobot(sim.Component):
    def __init__(self, layout: Layout, env: sim.Environment, y: float, z: float):
        super().__init__()

        self.layout = layout
        self.env = env

        self.x = 0
        self.y = y
        self.z = z
        self.t = env.now()

        self.next_y = y
        self.next_z = z
        self.next_t = env.now()

        sim.Animate3dBox(x_len=0.5, y_len=0.5, z_len=0.5, color="red", edge_color='white', x=self.x, y=self.y_func, z=self.z_func)

    def y_func(self, t: float):
        if self.next_t == self.t:
            return self.y
        else:
            return self.y + (self.next_y - self.y) * (t - self.t) / (self.next_t - self.t)

    def z_func(self, t: float):
        if self.next_t == self.t:
            return self.z
        else:
            return self.z + (self.next_z - self.z) * (t - self.t) / (self.next_t - self.t)

    def process(self) :
        duration = 1
        corridor_count = len(self.layout.corridors)  # numbers of t_corridors in a certain layout
        y_stock = 2 + corridor_count / 1.5

        while True:
            corridor_num = 0
            for corridor in self.layout.corridors:  # for each corridor in the layout, define the number of machines in left and right corridor
                y = (corridor_num + 0.5 - corridor_count / 2) * 2

                #Go to the RM inventory
                self.next_y = -y_stock
                self.next_t = self.env.now() + duration
                yield self.hold(duration)
                self.y = self.next_y

                # Move down in the RM inventory
                self.next_z = 1.25
                self.next_t = self.env.now() + duration
                yield self.hold(duration)
                self.z = self.next_z

                # Move up
                self.next_z = 2.5
                self.next_t = self.env.now() + duration
                yield self.hold(duration)
                self.z = self.next_z

                # Move to one WIP inventory
                self.next_y = y #I'm defining the next position to reach
                self.next_t = self.env.now() + duration
                yield self.hold(duration)
                self.y = self.next_y #and I'm ansking to maintain it

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

                corridor_num = corridor_num + 1

            # Go to the FP inventory
            self.next_y = y_stock
            self.next_t = self.env.now() + duration
            yield self.hold(duration)
            self.y = self.next_y

            # Move down in the RM inventory
            self.next_z = 1.25
            self.next_t = self.env.now() + duration
            yield self.hold(duration)
            self.z = self.next_z

            # Move up
            self.next_z = 2.5
            self.next_t = self.env.now() + duration
            yield self.hold(duration)
            self.z = self.next_z