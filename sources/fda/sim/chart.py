import matplotlib.pyplot as plt

from .machine import *
from .armrobot import *
from .mainrobot import *
from .order import *
from .job import *


def machineBarChart(sim_machines: list[SimMachine]):
    for sim_machine in sim_machines:
        waiting = sim_machine.state.value.value_duration('waiting') / 100
        mounting = sim_machine.state.value.value_duration('mounting') / 100
        unmounting = sim_machine.state.value.value_duration('unmounting') / 100
        working = sim_machine.state.value.value_duration('working') / 100
        returning = sim_machine.state.value.value_duration('returning') / 100

        categories = ['Waiting', 'Mounting', 'Unmounting', 'Working', 'Returning']
        values = [waiting, mounting, unmounting, working, returning]

        bar_width = 0.15

        # Graph
        position = range(len(MACHINES))
        for i in range(len(categories)):
            plt.bar([p + i * bar_width for p in position], values[i], width=bar_width, label=categories[i])

        # x Axis
        plt.xticks([])

        # Labels
        plt.xlabel('Machine')
        plt.ylabel('Utilisation (%)')
        plt.title('Machine Utilisation')

        # Legend
        plt.legend()

        # Print Graph
        plt.show()

        # TO SEE JUST ONE MACHINE PER CHART, THEN SUBSTITUTE MACHINES WITH sim_machines


def armRobotBarChart(sim_arm_robots: list[SimArmRobot]):
    for sim_arm_robot in sim_arm_robots:
        loading = sim_arm_robot.state_load.value.value_duration('loaded') / 100
        emptying = sim_arm_robot.state_load.value.value_duration('empty') / 100
        moving_x = sim_arm_robot.state_move.value.value_duration('moving_x') / 100
        moving_z = sim_arm_robot.state_move.value.value_duration('moving_z') / 100

        categories = ['Loading', 'Emptying', 'Moving_x', 'Moving_z']
        values = [loading, emptying, moving_x, moving_z]

        bar_width = 0.15

        # Graph
        position = range(len(sim_arm_robots))
        for i in range(len(categories)):
            plt.bar([p + i * bar_width for p in position], values[i], width=bar_width, label=categories[i])

        # x Axis
        plt.xticks([])

        # Labels
        plt.xlabel('Arm Robot')
        plt.ylabel('Robot State (%)')
        plt.title('Robot Load and Move State')

        # Legend
        plt.legend()

        # Print Graph
        plt.show()


def mainRobotBarChart(sim_main_robot: SimMainRobot):
    loading = sim_main_robot.state_load.value.value_duration('loaded') / 100
    empty = sim_main_robot.state_load.value.value_duration('empty') / 100
    moving_y = sim_main_robot.state_move.value.value_duration('moving_y') / 100
    moving_z = sim_main_robot.state_move.value.value_duration('moving_z') / 100

    categories = ['Loading', 'Empty', 'Moving_y', 'Moving_z']
    values = [loading, empty, moving_y, moving_z]

    bar_width = 0.15

    # Graph
    for i in range(len(values)):
        plt.bar(i*bar_width, values[i], width=bar_width, label=categories[i])

    # x Axis
    plt.xticks([])

    # Labels
    plt.xlabel('Main Robot')
    plt.ylabel('State (%)')
    plt.title('Main obot Load and Move State')

    # Legend
    plt.legend()

    # Print Graph
    plt.show()


def orderBarChart(jobs: list[SimJob]):
    for job in jobs:
        raw = job.state.value.value_duration('raw') / 100
        intermediate = job.state.value.value_duration('intermediate') / 100
        finished = job.state.value.value_duration('finished') / 100

        categories = ['Raw', 'Intermediate', 'Finished']
        values = [raw, intermediate, finished]

        bar_width = 0.15

        # Graph
        position = range(len(jobs))
        for i in range(len(categories)):
            plt.bar([p + i * bar_width for p in position], values[i], width=bar_width, label=categories[i])

        # x Axis
        plt.xticks([])

        # Labels
        plt.xlabel('Job state duration')
        plt.ylabel('State (%)')
        plt.title('Order state')

        # Legend
        plt.legend()

        # Print Graph
        plt.show()
