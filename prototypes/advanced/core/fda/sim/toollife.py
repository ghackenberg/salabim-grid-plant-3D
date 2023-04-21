import salabim as sim


from ..simulate import*
from ..model import *
from .job import *
from .remainingtoollife import *

class ToolLife(RemainingToolLife):
    def __init__(self, env: sim.Environment, x_dimension: float, x: float, y: float):
        super().__init__(env, x_dimension, x, y)

        # Remember remaining life units per tool
        self.remaining_tool_life_units: dict[ToolType, int] = {}
        # Iterate over all possible process steps for the given machine type
        for processStep in machine.machineType.processSteps:
            # Initialize the remaining life units for the respective tool type
            self.remaining_tool_life_units[processStep.toolType] = processStep.toolType.totalLifeUnits


    def process(self):
        value = self.remaining_tool_life_units[self.mounted_tool]
        while True:
            # Take next job from store
            job: Job = yield self.from_store(self.store_in)
            # Retrieve next process step to perform
            process_step = job.process_step_sequence.pop(0)
            # Duration of the process
            speed = self.ProcessStep.duration
            # Initial tool's life bar state
            yield from self.x(self.x_dimension, speed)
            # Remove own machine from machine sequence
            machine = job.machine_sequence.pop(0)
            # Assert that we are the machine to perform the step
            assert machine == self.machine
            # Check which tool is required
            self.mounted_tool = process_step.toolType
            # Check if previous tool is too old
            if self.remaining_tool_life_units[self.mounted_tool] > process_step.consumedToolLifeUnits:
                # Update remaining life units
                value = self.mounted_tool.totalLifeUnits
                yield from self.move_x(self.x_dimension * 0.3, speed)
            # TODO update tool life bar visualization
            elif self.remaining_tool_life_units[self.mounted_tool] < process_step.consumedToolLifeUnits:
                # End of total life unit
                yield from self.move_x(self.x_dimension * 0.1, speed)
                # TODO update tool life bar visualization
                # Update life units
                value = self.mounted_tool.totalLifeUnits
                yield from self.move_x(self.x_dimension * 0.3, speed)
            # Update remaining tool life units
            value = self.remaining_tool_life_units[self.mounted_tool] - process_step.consumedToolLifeUnits
            yield from self.move_x(self.x_dimension *  0.3, speed)

    '''
    def process (self):
        # Define duration of the processStep
        duration = self.ProcessStep.duration
        # Take next job from store
        job: Job = yield self.from_store(self.store_in)
        # Retrieve next process step to perform
        process_step = job.process_step_sequence.pop(0)
        # Remove own machine from machine sequence
        machine = job.machine_sequence.pop(0)
        # Assert that we are the machine to perform the step
        assert machine == self.machine
        # Define tool to use
        self.toolType = process_step.toolType
        max_totallife = self.toolType.totalLifeUnits
        self.
        # Visualize connection between tool and tool life bar
        # TODO white edge in the bar of the connected tool

        # Decrease the total life unit
        yield from self.move_x(self.next_x, duration)

        # Reset tool
        
        '''

