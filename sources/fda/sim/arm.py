import salabim as sim
import matplotlib.pyplot as plt

from ..model import Corridor, Machine

from .machine import SimMachine
from .armrobot import SimArmRobot


class SimArm(sim.Component):
    def setup(self, corridor: Corridor, machines: list[Machine], direction: str, store_in: sim.Store, store_out_1: sim.Store, store_out_2: sim.Store, dx: float, y: float):
        self.corridor = corridor
        self.machines = machines
        
        self.direction = direction

        self.store_in = store_in
        self.store_out_1 = store_out_1
        self.store_out_2 = store_out_2

        # Machines
        self.sim_machines: list[SimMachine] = []
        machine_num = 0
        for machine in machines:
            machine_x = (3 + machine_num * 2) * dx
            sim_machine = SimMachine(machine=machine, x=machine_x, y=y, env=self.env)
            self.sim_machines.append(sim_machine)
            machine_num = machine_num + 1

        # Transversal robot
        if len(machines) != 0:
            self.sim_arm_robot = SimArmRobot(corridor=corridor, machines=machines, direction=direction, store_in=store_in, store_out_arm=store_out_1, store_out_main=store_out_2, sim_machines=self.sim_machines, dx=dx, y=y, env=self.env)

        # Arm horizontal box
        if len(machines) != 0:
            x_len = len(machines) * 2 + 0.26
            x = (0.86 + x_len / 2) * dx
            sim.Animate3dBox(x_len=x_len, y_len=0.25, z_len=0.25, color="green", x=x, y=y, z=2.5)

        # Corridor storage arm vertical box
        if len(machines) != 0:
            sim.Animate3dBox(x_len=0.25, y_len=0.25, z_len=1.5, color="green", x=dx, y=y, z=1.625)
    
    def printStatistics(self):
        print(f"    - Arm {self.direction}:")
        if len(self.machines) != 0:
            self.sim_arm_robot.printStatistics()
        for sim_machine in self.sim_machines:
            sim_machine.printStatistics()
    
    def robotCount(self):
        if self.machineCount() > 0:
            return 1
        else:
            return 0

    def machineCount(self):
        return len(self.sim_machines)
    
    def robotUtilization(self):
        if self.machineCount() > 0:
            return self.sim_arm_robot.utilization()
        else:
            return 1

    def machineUtilization(self):
        cnt = self.machineCount()
        if cnt > 0:
            utl = 0
            for sim_machine in self.sim_machines:
                utl = utl + sim_machine.utilization() / cnt
            return utl
        else:
            return 1
    
    def plot(self):
        pass
