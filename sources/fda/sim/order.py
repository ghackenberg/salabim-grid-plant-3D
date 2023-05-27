import salabim as sim
from ..model import *
from .job import *

class SimOrder(sim.Component):
    def __init__(self, layout: Layout, scenario: Scenario, order: Order, env: sim.Environment, store_start: sim.Store):
        super().__init__()

        self.order = order
        
        self.sim_jobs: list[SimJob] = []
        for i in range(order.quantity):
            sim_job = SimJob(layout, scenario, order, i, env, store_start)
            self.sim_jobs.append(sim_job)

    def printStatistics(self):
        print(f" - Order {self.order.code}:")
        for sim_job in self.sim_jobs:
            sim_job.printStatistics()
