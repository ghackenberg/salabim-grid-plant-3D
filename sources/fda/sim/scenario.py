import salabim as sim
import matplotlib.pyplot as plt

from ..model import Layout, Scenario

from .order import SimOrder

class SimScenario(sim.Component):
    def __init__(self, layout: Layout, scenario: Scenario, env: sim.Environment, store_start: sim.Store):
        super().__init__()

        self.scenario = scenario
        
        self.sim_orders: list[SimOrder] = []
        for order in scenario.orders:
            sim_order = SimOrder(layout, scenario, order, env, store_start)
            self.sim_orders.append(sim_order)
    
    def printStatistics(self):
        print(f"{self.scenario.name}:")
        for sim_order in self.sim_orders:
            sim_order.printStatistics()
    
    def plot(self):
        rows = 1
        columns = len(self.sim_orders)

        plt.figure(self.scenario.name)

        col = 1
        for sim_order in self.sim_orders:
            plt.subplot(rows, columns, col)
            sim_order.plot()
            col = col + 1
