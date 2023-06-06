import salabim as sim
import matplotlib.pyplot as plt

from ..model import Layout, Scenario

from .corridor import SimCorridor
from .mainrobot import SimMainRobot


class SimLayout(sim.Component):
    def __init__(self, layout: Layout, scenario: Scenario, env: sim.Environment):
        super().__init__()

        self.layout = layout

        # Grid
        sim.Animate3dGrid(x_range=range(-20, 20), y_range=range(-20, 20))

        # Start and end storage boxes
        y = 2 + len(layout.corridors) / 1.15
        # ... start
        self.store_start = sim.Store("start")
        sim.Animate3dBox(x_len=3, y_len=1, z_len=1, color="yellow", x=0, y=y, z=0.5)
        # ... end
        self.store_end = sim.Store("end")
        sim.Animate3dBox(x_len=3, y_len=1, z_len=1, color="yellow", x=0, y=-y, z=0.5)

        # Start and end vertical boxes
        sim.Animate3dBox(x_len=0.25, y_len=0.25, z_len=1.5, color="red", x=0, y=y, z=1.625)
        sim.Animate3dBox(x_len=0.25, y_len=0.25, z_len=1.5, color="red", x=0, y=-y, z=1.625)

        # Main horizontal box
        sim.Animate3dBox(x_len=0.25, y_len=y*2.07, z_len=0.25, color="red", x=0, y=0, z=2.5)

        # Corridors
        self.sim_corridors: list[SimCorridor] = []
        corridor_num = 0
        for corridor in layout.corridors:
            y = (corridor_num + 0.5 - len(layout.corridors) / 2) * 2
            self.sim_corridors.append(SimCorridor(corridor, env, y))
            corridor_num = corridor_num + 1

        # Main robot
        self.sim_main_robot = SimMainRobot(layout, scenario, env, self.store_start, self.store_end, self.sim_corridors, 0, 2.5)
    
    def weight(self):
        weight = 0
        for sim_corridor in self.sim_corridors:
            weight = weight + sim_corridor.weight()
        return weight

    def utilization(self):
        weight = self.weight()
        if weight > 0:
            util = 0
            for sim_corridor in self.sim_corridors:
                if sim_corridor.weight() > 0:
                    util = util + sim_corridor.utilization() * sim_corridor.weight() / weight
            return util
        else:
            return 1

    def printStatistics(self):
        print(f"{self.layout.name}:")
        self.sim_main_robot.printStatistics()
        for sim_corridor in self.sim_corridors:
            sim_corridor.printStatistics()
    
    def plot(self, legend = False):
        plt.figure('Layout')

        rows = len(self.sim_corridors) + 1

        left = 0
        right = 0

        for sim_corridor in self.sim_corridors:
            left = max(left, len(sim_corridor.sim_arm_left.sim_machines))
            right = max(right, len(sim_corridor.sim_arm_right.sim_machines))
        
        if left > 0 and right > 0:
            columns = left + right + 2
        elif left > 0:
            columns = left + 1
        elif right > 0:
            columns = right + 1
        else:
            columns = 1

        # Main robot
        plt.subplot(rows, columns, 1)
        self.sim_main_robot.plot(legend)

        # Corridors
        row = 1
        for sim_corridor in self.sim_corridors:
            # Left arm
            col = 1
            if len(sim_corridor.sim_arm_left.sim_machines) > 0:
                # Robot
                plt.subplot(rows, columns, row * columns + col)
                sim_corridor.sim_arm_left.sim_arm_robot.plot(legend)
                col = col + 1
                # Machines
                for sim_machine in sim_corridor.sim_arm_left.sim_machines:
                    plt.subplot(rows, columns, row * columns + col)
                    sim_machine.plot(legend)
                    col = col + 1
            # Right arm
            col = 1 if left == 0 else left + 2
            if len(sim_corridor.sim_arm_right.sim_machines) > 0:
                # Robot
                plt.subplot(rows, columns, row * columns + col)
                sim_corridor.sim_arm_right.sim_arm_robot.plot(legend)
                col = col + 1
                # Machines
                for sim_machine in sim_corridor.sim_arm_right.sim_machines:
                    plt.subplot(rows, columns, row * columns + col)
                    sim_machine.plot(legend)
                    col = col + 1
            row = row + 1

        plt.show()
