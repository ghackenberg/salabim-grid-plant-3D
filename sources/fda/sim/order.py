import salabim as sim
import matplotlib.pyplot as plt

from ..model import Layout, Scenario, Order

from .job import SimJob


class SimOrder(sim.Component):
    def setup(self, layout: Layout, scenario: Scenario, order: Order, store_start: sim.Store):
        self.order = order
        
        self.sim_jobs: list[SimJob] = []
        for i in range(order.quantity):
            sim_job = SimJob(layout=layout, scenario=scenario, order=order, number=i, store_start=store_start, env=self.env)
            self.sim_jobs.append(sim_job)

    def printStatistics(self):
        print(f" - {self.order.name}:")
        for sim_job in self.sim_jobs:
            sim_job.printStatistics()
    
    def plot(self, legend = False):
        # Collect categories
        categories = []
        for job in self.sim_jobs:
            for value in job.state.value.values():
                if value not in categories:
                    categories.append(value)
        
        # Compute values
        values = [0 for c in categories]
        for job in self.sim_jobs:
            for value in job.state.value.values():
                duration = job.state.value.value_duration(value)
                index = categories.index(value)
                values[index] = values[index] + duration

        # Draw chart
        bar_width = 0.15

        # Graph
        for i in range(len(categories)):
            plt.bar(i * bar_width, values[i], width=bar_width, label=categories[i])

        # x Axis
        plt.xticks([])

        # Labels
        plt.xlabel('Order State')
        plt.ylabel('State Duration')
        plt.title(f'{self.order.name}')

        # Legend
        if legend:
            plt.legend()
