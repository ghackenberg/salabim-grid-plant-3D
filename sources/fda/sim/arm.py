import salabim as sim
import matplotlib.pyplot as plt

from ..model import Corridor, Machine

from .machine import SimMachine
from .armrobot import SimArmRobot


class SimArm(sim.Component):
    def __init__(self, corridor: Corridor, machines: list[Machine], name: str, env: sim.Environment, store_in: sim.Store, store_out_1: sim.Store, store_out_2: sim.Store, dx: float, y: float):
        super().__init__(name)

        self.corridor = corridor
        self.machines = machines

        self.env = env

        self.store_in = store_in
        self.store_out_1 = store_out_1
        self.store_out_2 = store_out_2

        # Machines
        self.sim_machines: list[SimMachine] = []
        machine_num = 0
        for machine in machines:
            machine_x = (3 + machine_num * 2) * dx
            sim_machine = SimMachine(machine, env, machine_x, y)
            self.sim_machines.append(sim_machine)
            machine_num = machine_num + 1

        # Transversal robot
        if len(machines) != 0:
            self.sim_arm_robot = SimArmRobot(corridor, machines, env, store_in, store_out_1, store_out_2, self.sim_machines, dx, y)

        # Arm horizontal box
        if len(machines) != 0:
            x_len = len(machines) * 2 + 0.26
            x = (0.86 + x_len / 2) * dx
            sim.Animate3dBox(x_len=x_len, y_len=0.25, z_len=0.25, color="green", x=x, y=y, z=2.5)

        # Corridor storage arm vertical box
        if len(machines) != 0:
            sim.Animate3dBox(x_len=0.25, y_len=0.25, z_len=1.5, color="green", x=dx, y=y, z=1.625)
    
    def printStatistics(self):
        print(f"    - Arm {self.name()}:")
        if len(self.machines) != 0:
            self.sim_arm_robot.printStatistics()
        for sim_machine in self.sim_machines:
            sim_machine.printStatistics()
        machineBarChart(self.corridor, self.name(), self.sim_machines)
        armRobotBarChart(self.corridor, self.name(), self.sim_arm_robot)


def machineBarChart(corridor: Corridor, name: str, sim_machines: list[SimMachine]):
    categories = ['Waiting', 'Mounting', 'Unmounting', 'Working', 'Returning']

    for sim_machine in sim_machines:
        waiting = sim_machine.state.value.value_duration('waiting')
        mounting = sim_machine.state.value.value_duration('mounting')
        unmounting = sim_machine.state.value.value_duration('unmounting')
        working = sim_machine.state.value.value_duration('working')
        returning = sim_machine.state.value.value_duration('returning')

        values = [waiting, mounting, unmounting, working, returning]

        bar_width = 0.15

        # Graph
        position = range(len(sim_machines))
        for i in range(len(categories)):
            plt.bar([p + i * bar_width for p in position], values[i], width=bar_width, label=categories[i])

        # x Axis
        plt.xticks([])

        # Labels
        plt.xlabel('Machine State')
        plt.ylabel('State Duration')
        plt.title(f'{corridor.name} / Arm {name} / {sim_machine.machine.name}')

        # Legend
        plt.legend()

        # Print Graph
        plt.show()


def armRobotBarChart(corridor: Corridor, name: str, sim_arm_robot: SimArmRobot):
    categories = ['Loaded', 'Empty', 'Waiting', 'Moving_x', 'Moving_y', 'Moving_z']

    loaded = sim_arm_robot.state_load.value.value_duration('loaded')
    empty = sim_arm_robot.state_load.value.value_duration('empty')
    waiting = sim_arm_robot.state_move.value.value_duration('waiting')
    moving_x = sim_arm_robot.state_move.value.value_duration('moving_x')
    moving_y = sim_arm_robot.state_move.value.value_duration('moving_y')
    moving_z = sim_arm_robot.state_move.value.value_duration('moving_z')

    values = [loaded, empty, waiting, moving_x, moving_y, moving_z]

    bar_width = 0.15

    # Graph
    for i in range(len(categories)):
        plt.bar(i * bar_width, values[i], width=bar_width, label=categories[i])

    # x Axis
    plt.xticks([])

    # Labels
    plt.xlabel('Robot Load and Move State')
    plt.ylabel('State Duration')
    plt.title(f'{corridor.name} / Arm {name} / Robot')

    # Legend
    plt.legend()

    # Print Graph
    plt.show()
