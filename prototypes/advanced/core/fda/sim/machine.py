import salabim as sim

from .job import *
from .tool import *
from ..model import *


class SimMachine(sim.Component):
    def __init__(self, machine: Machine, env: sim.Environment, store_in: sim.Store, store_out: sim.Store, x: float,
                 y: float):
        super().__init__()

        # Remember machine
        self.machine = machine

        # Remember remaining life units per tool
        self.remaining_tool_life_units: dict[ToolType, int] = {}
        self.remaining_tool_life_units_t: dict[ToolType, float] = {}
        self.remaining_tool_life_units_next: dict[ToolType, int] = {}
        self.remaining_tool_life_units_next_t: dict[ToolType, float] = {}
        # Iterate over all possible process steps for the given machine type
        for processStep in machine.machineType.processSteps:
            # Initialize the remaining life units for the respective tool type
            self.remaining_tool_life_units[processStep.toolType] = processStep.toolType.totalLifeUnits
            self.remaining_tool_life_units_t[processStep.toolType] = env.now()
            self.remaining_tool_life_units_next[processStep.toolType] = processStep.toolType.totalLifeUnits
            self.remaining_tool_life_units_next_t[processStep.toolType] = env.now()

        # Remember currently mounted tool
        self.mounting = False
        self.unmouting = False
        self.mounted_tool: ToolType = None

        # Remember current unavailability
        self.unavailability = 0
        self.total_availability = 24  # assuming one whole day of avalability menus the unavailability
        # Remember machine utilization
        self.effective_machine_utilisation = 0
        self.machine_utilization = 0

        self.env = env

        # Remember store in
        self.store_in = store_in
        # Remember store out
        self.store_out = store_out



        # Down
        sim.Animate3dBox(x_len=0.25, y_len=0.25, z_len=1.20, color="green", x=x, y=y + 0.00, z=1.80)

        # Tool Support
        sim.Animate3dBox(x_len=0.05, y_len=0.18, z_len=0.05, color="white", x=x, y=y + 0.19, z=1.18)
        sim.Animate3dBox(x_len=0.60, y_len=0.18, z_len=0.05, color="white", x=x, y=y + 0.19, z=1.18)
        # Tool Visualization
        m = 0
        i = 0
        color = ['blue', 'red', 'black', 'yellow', ' green', 'pink', 'chocolate', 'indigo', 'teal', 'darksalmon',
                 'lavender', 'darkgoldenrod', 'powderblue', 'thistle', 'gainsayer']
        for tool_type in MACHINETYPE_TOOLTYPE_MAP[machine.machineType]:
            sim.Animate3dBox(x_len=0.05, y_len=0.05, z_len=0.18, color=color[i], x=x + m, y=y + 0.25, z=1.10)
            m = m + 0.1
            i = i + 1

        # Life Bar visualization
        z_bar = 0.70
        for self.mounted_tool in self.remaining_tool_life_units:
            sim.Animate3dBox(x_len=lambda t: self.x_func(tool_type, t), y_len=0.01, z_len=0.07,
                             color=lambda t: self.c_func(tool_type), x=x, y=y + 0.4379, z=z_bar)
            z_bar = z_bar - 0.08
        # Machine
        sim.Animate3dBox(x_len=0.60, y_len=0.40, z_len=0.40, color="white", x=x, y=y - 0.08, z=1.00)
        sim.Animate3dBox(x_len=0.60, y_len=0.70, z_len=0.60, color="white", x=x, y=y + 0.08, z=0.50)

        # TODO add visualization for progress of process step


    def x_func(self, tool_type: ToolType, t: float):
        rtlu = self.remaining_tool_life_units[tool_type]
        rtlu_t = self.remaining_tool_life_units_t[tool_type]
        rtlu_next = self.remaining_tool_life_units_next[tool_type]
        rtlu_next_t = self.remaining_tool_life_units_next_t[tool_type]
        if rtlu_next_t == rtlu_t:
            return rtlu / tool_type.totalLifeUnits * 0.4
        else:
            return (rtlu + (rtlu_next - rtlu) * (t - rtlu_t) / (rtlu_next_t - rtlu_t)) / tool_type.totalLifeUnits * 0.4

    def c_func(self, tool_type: ToolType):
        rtlu_t = self.remaining_tool_life_units_t[tool_type]
        rtlu_next_t = self.remaining_tool_life_units_next_t[tool_type]
        if tool_type == self.mounted_tool:
            if rtlu_t == rtlu_next_t:
                if self.unmouting:
                    return "orange"
                elif self.mounting:
                    return "yellow"
                else:
                    return "green"
            else:
                return "red"
        else:
            return "gray"

    def statistic(self, jobs: list[Job]):
        for job in jobs:
            processes = job.process_step_sequence
            machines = job.machine_sequence

            utilisation: list[tuple[str, float]] = []

            for machine in machines:
                for process in processes:
                    duration = process.duration
                    if self.machine == process.machineType.machines:
                        self.effective_machine_utilisation = self.effective_machine_utilisation + duration

                self.machine_utilization = self.effective_machine_utilisation / self.total_availability
                utilisation.append(f"{machine.machineType} : {self.machine_utilization}")
        return utilisation

    def process(self):
        while True:
            # Take next job from store
            job: Job = yield self.from_store(self.store_in)
            # Retrieve next process step to perform
            process_step = job.process_step_sequence.pop(0)

            duration = process_step.duration
            consumed_life_units = process_step.consumedToolLifeUnits
            tool_type = process_step.toolType
            total_life_units = tool_type.totalLifeUnits
            mount_time = tool_type.mountTime
            unmount_time = tool_type.unmountTime
            remaining_life_units = self.remaining_tool_life_units[tool_type]

            # Remove own machine from machine sequence
            machine = job.machine_sequence.pop(0)
            # Assert that we are the machine to perform the step
            assert machine == self.machine
            # Check if tool is mounted
            if tool_type != self.mounted_tool:
                # Check if tool is mounted
                if self.mounted_tool is None:
                    self.unmouting = True
                    # Unmount tool
                    yield self.hold(unmount_time)
                    # TODO update tool visualization
                    self.unmouting = False
                self.mounting = True
                # Update mounted tool
                self.mounted_tool = tool_type
                # Mount tool
                yield self.hold(mount_time)
                self.mounting = False
                # Check if previous tool is too old
                if remaining_life_units < consumed_life_units:
                    # Update remaining life units
                    remaining_life_units = total_life_units
                # TODO update tool visualization
            elif remaining_life_units < consumed_life_units:
                self.unmouting = True
                # Unmount tool
                yield self.hold(unmount_time)
                # TODO update tool visualization
                self.unmouting = False
                self.mounting = True
                # Remount tool
                yield self.hold(mount_time)
                self.mounting = False
                # Update life units
                remaining_life_units = total_life_units
            # Machine unavailability
            self.unavailability = self.unavailability + mount_time + unmount_time
            self.total_availability = self.total_availability - self.unavailability
            # Prepare animation
            self.remaining_tool_life_units[tool_type] = remaining_life_units
            self.remaining_tool_life_units_t[tool_type] = self.env.now()
            self.remaining_tool_life_units_next[tool_type] = remaining_life_units - consumed_life_units
            self.remaining_tool_life_units_next_t[tool_type] = self.env.now() + duration
            # Perform process step
            yield self.hold(duration)
            # Update job state
            job.state = process_step.producesProductType
            # Update remaining tool life units
            self.remaining_tool_life_units[tool_type] = remaining_life_units - consumed_life_units
            self.remaining_tool_life_units_t[tool_type] = self.env.now()
            self.remaining_tool_life_units_next[tool_type] = remaining_life_units - consumed_life_units
            self.remaining_tool_life_units_next_t[tool_type] = self.env.now()
            # Place job back to store
            yield self.to_store(self.store_out, job)

'''
    def statistic(self, job: Job):
        print("inizio metodo")
        
        processes = job.process_step_sequence
        machines = job.machine_sequence

        utilisation: list[tuple[str, float]] = []
        print('aa')
        for self.machine in machines:
            print('a')
            for process in processes:
                print('b')
                duration = process.duration
                if self.machine == process.machineType.machines:
                    self.effective_machine_utilisation = self.effective_machine_utilisation + duration
                    print('c')
            self.machine_utilization = self.effective_machine_utilisation / self.total_availability
            utilisation.append(f"{self.machine} : {self.machine_utilization}")
        return utilisation
        '''





