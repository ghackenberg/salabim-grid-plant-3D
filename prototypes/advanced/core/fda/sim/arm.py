import salabim as sim

from ..model import *
from .machine import *
from .traversalrobot import *

class SimArm(sim.Component):
    def __init__(self, corridor: Corridor, machines: list[Machine], name: str, env: sim.Environment, store_in: sim.Store, store_out_1: sim.Store, store_out_2: sim.Store, dx: float, y: float):
        super().__init__(name)

        # CORRIDOR
        self.corridor = corridor

        # MACHINES
        self.machines = machines

        # ENVIRONMENT
        self.env = env

        # STORE
        self.store_in = store_in
        self.store_out_1 = store_out_1
        self.store_out_2 = store_out_2

        # SIM MACHINES
        self.sim_machines: list[SimMachine] = []
        machine_num = 0
        for machine in machines:
            machine_x = (3 + machine_num * 2) * dx
            sim_machine = SimMachine(machine, env, machine_x, y)
            self.sim_machines.append(sim_machine)
            machine_num = machine_num + 1

        # TRANSVERSAL ROBOT
        if len(machines) != 0:
            TransversalRobot(corridor, machines, env, store_in, store_out_1, store_out_2, self.sim_machines, dx, y)

        # HORIZONTAL BOX
        if len(machines) != 0:
            x_len = len(machines) * 2 + 0.26
            x = (0.86 + x_len / 2) * dx
            sim.Animate3dBox(x_len=x_len, y_len=0.25, z_len=0.25, color="green", x=x, y=y, z=2.5)

        # VERTICAL BOX
        if len(machines) != 0:
            sim.Animate3dBox(x_len=0.25, y_len=0.25, z_len=1.5, color="green", x=dx, y=y, z=1.625)
    
    def printStatistics(self):
        print(f" - Arm {self.name()}:")
        for sim_machine in self.sim_machines:
            sim_machine.printStatistics()