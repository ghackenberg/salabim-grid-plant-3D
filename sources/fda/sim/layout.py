import salabim as sim
from ..model import *
from .corridor import *
from .mainrobot import *

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

    def printStatistics(self):
        print(f"{self.layout.name}:")
        self.sim_main_robot.printStatistics()
        for sim_corridor in self.sim_corridors:
            sim_corridor.printStatistics()
