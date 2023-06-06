import salabim as sim
import matplotlib.pyplot as plt

from ..model import Layout, Scenario, Order

from .job import SimJob


class SimOrder(sim.Component):
    def __init__(self, layout: Layout, scenario: Scenario, order: Order, env: sim.Environment, store_start: sim.Store):
        super().__init__()

        self.order = order
        
        self.sim_jobs: list[SimJob] = []
        for i in range(order.quantity):
            sim_job = SimJob(layout, scenario, order, i, env, store_start)
            self.sim_jobs.append(sim_job)

    def printStatistics(self):
        print(f" - {self.order.name}:")
        for sim_job in self.sim_jobs:
            sim_job.printStatistics()
        #orderBarChart(self.sim_jobs)


def orderBarChart(jobs: list[SimJob]):
    categories = ['Raw', 'Intermediate', 'Finished']

    for job in jobs:
        raw = job.state.value.value_duration('raw')
        intermediate = job.state.value.value_duration('intermediate')
        finished = job.state.value.value_duration('finished')

        values = [raw, intermediate, finished]

        bar_width = 0.15

        # Graph
        position = range(len(jobs))
        for i in range(len(categories)):
            plt.bar([p + i * bar_width for p in position], values[i], width=bar_width, label=categories[i])

        # x Axis
        plt.xticks([])

        # Labels
        plt.xlabel('Job state duration')
        plt.ylabel('State (%)')
        plt.title('Order state')

        # Legend
        plt.legend()

        # Print Graph
        plt.show()
