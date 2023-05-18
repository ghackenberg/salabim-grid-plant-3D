import salabim as sim

from ..model import *
from .machine import *


def utilisation_values(processes: list[ProcessStep], machines: list[Machine], layout: Layout, total_availability):
    utilisation = []
    for machine in machines:
        if machine.corridor.layout == layout:
            effective_machine_utilisation = 0
            machine_utilisation = 0
            for processStep in processes:
                if machine in processStep.machineType.machines:
                    duration = processStep.duration
                    effective_machine_utilisation = effective_machine_utilisation + duration
                    machine_utilisation = effective_machine_utilisation / total_availability
            utilisation.append({machine: machine_utilisation})

            return utilisation
