import salabim as sim
import random

from ..model import *
from ..calculate import *

class Job(sim.Component):
    def __init__(self, layout: Layout, scenario: Scenario, order: Order, store: sim.Store):
        super().__init__()

        self.layout = layout
        self.scenario = scenario
        self.order = order

        self.store = store

        # Calculate processes
        process_step_sequences = calculateProcessStepSequences(order.productType)
        # Pick random process
        self.process_step_sequence = process_step_sequences[random.randint(0, len(process_step_sequences) - 1)]
        
        # Calculate routes for that process
        machine_sequences = calculateMachineSequencesFromProcessStepSequence(self.process_step_sequence, self.layout)
        # Pick random route
        self.machine_sequence = machine_sequences[random.randint(0, len(machine_sequences) - 1)]

        # Define job state
        self.state = self.process_step_sequence[0].consumesProductType

    def process(self):
        # Put into store
        yield self.to_store(self.store, self)