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
        self.processes = calculateProcesses(order.productType)
        # Pick random process
        self.process = self.processes[random.randint(0, len(self.processes) - 1)]
        # Calculate routes for that process
        self.routes = calculateProcessRoutes(self.process, self.layout)
        # Pick random route
        self.route = self.routes[random.randint(0, len(self.routes) - 1)]

    def process(self):
        # Put into store
        yield self.to_store(self.store, self)