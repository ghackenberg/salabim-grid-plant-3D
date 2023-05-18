from .machine import *


def utilisation(processes: list[ProcessStep], machines: list[Machine], layout: Layout, total_availability):
    U = []
    for machine in machines:
        if machine.corridor.layout == layout:
            effective_machine_utilisation = 0
            machine_utilisation = 0
            for processStep in processes:
                if machine in processStep.machineType.machines:
                    duration = processStep.duration
                    effective_machine_utilisation = effective_machine_utilisation + duration
                    machine_utilisation = machine_utilisation + effective_machine_utilisation / total_availability
            U.append({machine: machine_utilisation})

            return U
