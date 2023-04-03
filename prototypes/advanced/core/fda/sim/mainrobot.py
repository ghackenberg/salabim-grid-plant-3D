import salabim as sim

from ..model import *
from .robot import *


class MainRobot(Robot):
    def __init__(self, layout: Layout, scenario: Scenario, env: sim.Environment, y: float, z: float):
        super().__init__(env, 0, y, z, "red")

        self.layout = layout
        self.scenario = scenario

    def process(self) :
        duration = 1
        corridor_count = len(self.layout.corridors)  # numbers of t_corridors in a certain layout
        y_stock = 2 + corridor_count / 1.5

        while True:
            corridor_num = 0
            for corridor in self.layout.corridors:  # for each corridor in the layout, define the number of machines in left and right corridor
                y = (corridor_num + 0.5 - corridor_count / 2) * 2

                #Go to the RM inventory
                yield from self.move_y(-y_stock, duration)
                # Move down in the RM inventory
                yield from self.move_z(1.25, duration)
                # Move up
                yield from self.move_z(2.5, duration)
                # Move to one WIP inventory
                yield from self.move_y(y, duration)
                # Move down
                yield from self.move_z(1.25, duration)
                # Move up
                yield from self.move_z(2.5, duration)

                corridor_num = corridor_num + 1