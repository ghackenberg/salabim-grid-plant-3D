import salabim as sim
import random

from ..calculate import calculateOperationSequences, calculateMachineSequencesFromOperationSequence
from ..model import Layout, Scenario, Order
from ..util import toString


class SimJob(sim.Component):
    def __init__(self, layout: Layout, scenario: Scenario, order: Order, number: int, store_start: sim.Store, *args, **kwargs):
        super().__init__(*args, **kwargs)

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
        self.state = sim.State("State", value=value, env=self.env)

    def process(self):
        # Debug output
        print(f"[t={self.env.now()}] Scheduling order {self.order.name} job {self.number}")
        # Put into start store
        yield self.to_store(self.store_start, self)
        # Debug output
        print(f"[t={self.env.now()}] Order {self.order.name} job {self.number} scheduled")
    
    def printStatistics(self):
        output = toString(self.state)
        print(f"    - Job {self.number} ({output})")
