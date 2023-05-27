import salabim as sim
from ..model import *
from .corridor import *
from .mainrobot import *

class SimLayout(sim.Component):
    def __init__(self, layout: Layout, scenario: Scenario, env: sim.Environment):
        super().__init__()

        # GRID
        sim.Animate3dGrid(x_range=range(-20, 20), y_range=range(-20, 20))

        # MAIN STORAGES
        y = 2 + len(layout.corridors) / 1.15
        # ... start
        self.store_start = sim.Store("start")
        sim.Animate3dBox(x_len=3, y_len=1, z_len=1, color="yellow", x=0, y=y, z=0.5)
        # ... end
        self.store_end = sim.Store("end")
        sim.Animate3dBox(x_len=3, y_len=1, z_len=1, color="yellow", x=0, y=-y, z=0.5)

        # MAIN CORRIDOR (vertical)
        sim.Animate3dBox(x_len=0.25, y_len=0.25, z_len=1.5, color="red", x=0, y=y, z=1.625)
        sim.Animate3dBox(x_len=0.25, y_len=0.25, z_len=1.5, color="red", x=0, y=-y, z=1.625)

        # MAIN CORRIDOR (horizontal)
        sim.Animate3dBox(x_len=0.25, y_len=y*2.07, z_len=0.25, color="red", x=0, y=0, z=2.5)

        # CORRIDORS
        self.sim_corridors: list[SimCorridor] = []
        corridor_num = 0
        for corridor in layout.corridors:
            y = (corridor_num + 0.5 - len(layout.corridors) / 2) * 2
            self.sim_corridors.append(SimCorridor(corridor, env, y))
            corridor_num = corridor_num + 1

        # MAIN ROBOT
        self.main_robot = MainRobot(layout, scenario, env, self.store_start, self.store_end, self.sim_corridors, 0, 2.5)

    def printStatistics(self):
        for sim_corridor in self.sim_corridors:
            sim_corridor.printStatistics()
