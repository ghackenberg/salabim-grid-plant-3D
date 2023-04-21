import salabim as sim

from ..simulate import*
from ..model import *
from .job import *
from .toollife import *


class SimMachine(sim.Component):
    def __init__(self, machine: Machine, store_in: sim.Store, store_out: sim.Store, x: float, y: float):
        super().__init__()

        # Remember machine
        self.machine = machine

        # Remember remaining life units per tool
        self.remaining_tool_life_units: dict[ToolType, int] = {}
        # Iterate over all possible process steps for the given machine type
        for processStep in machine.machineType.processSteps:
            # Initialize the remaining life units for the respective tool type
            self.remaining_tool_life_units[processStep.toolType] = processStep.toolType.totalLifeUnits
        
        # Remember currently mounted tool
        self.mounted_tool: ToolType = None

        # Remember store in
        self.store_in = store_in
        # Remember store out
        self.store_out = store_out

        #Available color
        color = ['blue', 'black', 'red', 'yellow', ' green', 'pink', 'indigo', 'chocolate', 'teal', 'darksalmon',
                 'lavander', 'darkgoldenrod', 'powderblue', 'thistel', 'gainsboro']

        # Down
        sim.Animate3dBox(x_len=0.25, y_len=0.25, z_len=1.20, color="green", x=x, y=y+0.00, z=1.80)

        # Tool
        sim.Animate3dBox(x_len=0.05, y_len=0.18, z_len=0.05, color="white", x=x, y=y + 0.19, z=1.18)
        sim.Animate3dBox(x_len=0.60, y_len=0.18, z_len=0.05, color="white", x=x, y=y + 0.19, z=1.18)

        z_bar = 0.70
        for toolType in MACHINETYPE_TOOLTYPE_MAP[machine.machineType]:
            # Background tool life bar
            sim.Animate3dBox(x_len=0.459, y_len=0.01, z_len=0.07, color='gray', x=x, y=y + 0.4379, z=z_bar)
            z_bar = z_bar - 0.08
            # TODO understand how to distribute the tools around the center /
            #  (one on the left, one on the right, and then again), instead of all on the left
            # TODO add visualization tools' remaining life units

        # Machine
        sim.Animate3dBox(x_len=0.60, y_len=0.40, z_len=0.40, color="white", x=x, y=y-0.08, z=1.00)
        sim.Animate3dBox(x_len=0.60, y_len=0.70, z_len=0.60, color="white", x=x, y=y+0.08, z=0.50)

        # TODO add visualization for progress of process step

    def process(self):
        while True:
            # Take next job from store
            job: Job = yield self.from_store(self.store_in)
            # Retrieve next process step to perform
            process_step = job.process_step_sequence.pop(0)
            # Remove own machine from machine sequence
            machine = job.machine_sequence.pop(0)
            # Assert that we are the machine to perform the step
            assert machine == self.machine
            # Check if tool is mounted
            if process_step.toolType != self.mounted_tool:
                # Check if tool is mounted
                if self.mounted_tool != None:
                    # Unmount tool
                    yield self.hold(self.mounted_tool.unmountTime)
                    # TODO update tool visualization
                # Mount tool
                yield self.hold(process_step.toolType.mountTime)
                # Update mounted tool
                self.mounted_tool = process_step.toolType
                # Check if previous tool is too old
                if self.remaining_tool_life_units[self.mounted_tool] < process_step.consumedToolLifeUnits:
                    # Update remaining life units
                    self.remaining_tool_life_units[self.mounted_tool] = self.mounted_tool.totalLifeUnits
                # TODO update tool visualization
            elif self.remaining_tool_life_units[self.mounted_tool] < process_step.consumedToolLifeUnits:
                # Unmount tool
                yield self.hold(self.mounted_tool.unmountTime)
                # TODO update tool visualization
                # Remount tool
                yield self.hold(self.mounted_tool.mountTime)
                # Update life units
                self.remaining_tool_life_units[self.mounted_tool] = self.mounted_tool.totalLifeUnits
            # Perform process step
            yield self.hold(process_step.duration)
            # Update job state
            job.state = process_step.producesProductType
            # Update remaining tool life units
            self.remaining_tool_life_units[self.mounted_tool] = self.remaining_tool_life_units[self.mounted_tool] - process_step.consumedToolLifeUnits
            # Place job back to store
            yield self.to_store(self.store_out, job)
