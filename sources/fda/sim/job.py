import salabim as sim
import random

from ..calculate import *
from ..model import *
from ..util import *


class SimJob(sim.Component):
    def __init__(self, layout: Layout, scenario: Scenario, order: Order, number: int, env: sim.Environment, store_start: sim.Store):
        super().__init__()

        self.env = env

        self.layout = layout
        self.scenario = scenario
        self.order = order
        self.number = number

        self.store_start = store_start

        # Calculate processes
        operation_sequences = calculateOperationSequences(order.product_type)
        # Pick random process
        self.operation_sequence = operation_sequences[random.randint(0, len(operation_sequences) - 1)]
        
        # Calculate routes for that process
        machine_sequences = calculateMachineSequencesFromOperationSequence(self.operation_sequence, self.layout)
        # Pick random route
        self.machine_sequence = machine_sequences[random.randint(0, len(machine_sequences) - 1)]

        # Track state
        value = self.operation_sequence[0].consumes_product_type.name
        self.state = sim.State("State", value=value)

    def process(self):
        # Put into start store
        yield self.to_store(self.store_start, self)
    
    def printStatistics(self):
        output = toString(self.state)
        print(f"    - Job {self.number} ({output})")
