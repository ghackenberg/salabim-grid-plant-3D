import matplotlib.pyplot as plt

from .machine import *

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

        # Labels
        plt.xlabel('Machine')
        plt.ylabel('Utilisation (%)')
        plt.title('Machine Utilisation')

        # Legend
        plt.legend()

        # Print Graph
        plt.xticks([p + bar_width * (len(categories) - 1) / 2 for p in position], MACHINES)
        plt.show()

