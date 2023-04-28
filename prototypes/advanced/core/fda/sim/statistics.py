import salabim as sim

from .machine import *
from .job import *
from ..model import *

def Statistics(job: Job):
    env = sim.Environment(time_unit='hours')

    processes = job.process_step_sequence
    machines = job.machine_sequence
    duration = processes.duration


    unavailability = processes.toolType.mountTime + processes.toolType.unmountTime
    total_availability = yield 24 - unavailability

    #machine_utilization = availability / total_availability

    #utilization: list['MachineType': float] = []
    #oppure
    utilization: list[MachineType] = []
    print('aa')
    for machine in machines:
        effective_machine_utilization = 0
        print('a')
        for process in processes:
            print('b')
            if machine in process:
                effective_machine_utilization = effective_machine_utilization + duration
                print ('c')
        machine_utilization = effective_machine_utilization / total_availability
        utilization.append(machine_utilization)
    return utilization




'''
        name = sim.Pdf(('John', 30, 'Peter', 20, 'Mike', 20, 'Andrew', 20, 'Ruud', 5, 'Jan', 5)).sample()
        monitor_names.tally(name)

    monitor_names.print_histogram(values=True)




class Utilization(sim.Monitor):
    # Total available time per each machine
    machine_total = 480
    # Effective used time per each machine
    machine_effective = 200
    # Utilization = effective used time / total available time
    utilization = machine_effective/machine_total
    # Overall plant utilization = SUM(effective used time) / number of machines


print(Utilization)

utilization = sim.Monitor('utilization')
utilization.tally(this_duration)

utilization.print_statistics()
'''