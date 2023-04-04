import salabim as sim

from ..model import *
from .job import *

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

        # Down
        sim.Animate3dBox(x_len=0.25, y_len=0.25, z_len=1.20, color="green", x=x, y=y, z=1.8)
        # Tool
        sim.Animate3dBox(x_len=0.05, y_len=0.05, z_len=0.18, color="blue", x=x, y=y+0.25, z=1.1)
        sim.Animate3dBox(x_len=0.05, y_len=0.18, z_len=0.05, color="white", x=x, y=y + 0.19, z=1.18)
        # Machine
        sim.Animate3dBox(x_len=0.60, y_len=0.40, z_len=0.40, color="white", x=x, y=y-0.08 , z=1)
        sim.Animate3dBox(x_len=0.60, y_len=0.70, z_len=0.60, color="white", x=x, y=y+0.08, z=0.5)

    def process(self):
        while True:
            # Take next job from store
            job: Job = yield self.from_store(self.store_in)
            # Retrieve next process step to perform
            step = job.steps.pop(0)
            # Check if tool is mounted
            if step.toolType != self.mounted_tool:
                # Check if tool is mounted
                if self.mounted_tool != None:
                    # Unmount tool
                    yield self.hold(self.mounted_tool.unmountTime)
                # Mount tool
                yield self.hold(step.toolType.mountTime)
                # Update mounted tool
                self.mounted_tool = step.toolType
                # Check if previous tool is too old
                if self.remaining_tool_life_units[self.mounted_tool] < step.consumedToolLifeUnits:
                    # Update remaining life units
                    self.remaining_tool_life_units[self.mounted_tool] = self.mounted_tool.totalLifeUnits
            elif self.remaining_tool_life_units[self.mounted_tool] < step.consumedToolLifeUnits:
                # Unmount tool
                yield self.hold(self.mounted_tool.unmountTime)
                # Remount tool
                yield self.hold(self.mounted_tool.mountTime)
                # Update life units
                self.remaining_tool_life_units[self.mounted_tool] = self.mounted_tool.totalLifeUnits
            # Perform process step
            yield self.hold(step.duration)
            # Update job state
            job.state = step.producesProductType
            # Update remaining tool life units
            self.remaining_tool_life_units[self.mounted_tool] = self.remaining_tool_life_units[self.mounted_tool] - step.consumedToolLifeUnits
            # Place job back to store
            yield self.to_store(self.store_out, job)
