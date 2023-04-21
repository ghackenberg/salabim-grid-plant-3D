import salabim as sim

from ..model import *
from ..calculate import *
from .robot import *
from .job import *
from .tool import *
from .machine import *

class ToolSwitch(ToolMov):
    def __init__(self, layout: Layout, scenario: Scenario, env: sim.Environment, x: float):
        super().__init__(env, x)

        self.layout = layout
        self.scenario = scenario

    def process (self):
        m = 0
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
                yield from self.move_x(self.x + m, self.toolType.unmountTime) #switch the tool. x is the center of the machine
                # TODO how to define m?
            else:
                # Mount tool
                yield from self.move_x(self.SimMachine.x, self.toolType.mountTime)
            # Update mounted tool
            self.mounted_tool = process_step.toolType
        elif process_step.toolType == self.mounted_tool:
            yield self.move_x(self.x, self.processStep.duration)
