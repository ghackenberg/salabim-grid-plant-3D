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
        self.steps_options = calculateProcesses(order.productType)
        # Pick random process
        self.steps = self.steps_options[random.randint(0, len(self.steps_options) - 1)]
        
        # Calculate routes for that process
        self.route_options = calculateProcessRoutes(self.steps, self.layout)
        # Pick random route
        self.route = self.route_options[random.randint(0, len(self.route_options) - 1)]

        # Define job state
        self.state = self.steps[0].consumesProductType

    def process(self):
        # Put into store
        yield self.to_store(self.store, self)