import salabim as sim
import matplotlib.pyplot as plt

from ..model import Layout, Scenario

from .order import SimOrder

class SimScenario(sim.Component):
    def setup(self, layout: Layout, scenario: Scenario, store_start: sim.Store):
        self.scenario = scenario
        
        self.sim_orders: list[SimOrder] = []
        for order in scenario.orders:
            sim_order = SimOrder(layout=layout, scenario=scenario, order=order, store_start=store_start, env=self.env)
            self.sim_orders.append(sim_order)
    
    def printStatistics(self):
        print(f"{self.scenario.name}:")
        for sim_order in self.sim_orders:
            sim_order.printStatistics()
    
    def plot(self, legend = False):
        rows = 1
        columns = len(self.sim_orders)

        plt.figure(self.scenario.name)

        col = 1
        for sim_order in self.sim_orders:
            plt.subplot(rows, columns, col)
            sim_order.plot(legend)
            col = col + 1
