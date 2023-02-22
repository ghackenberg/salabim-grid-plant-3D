import networkx
import matplotlib

from .model import *

def toNetworkXBasic():
    graph = networkx.Graph()

    for machineType in MACHINE_TYPES:
        graph.add_node(machineType.name)
    for toolType in TOOL_TYPES:
        graph.add_node(toolType.name)
    for productType in PRODUCT_TYPES:
        graph.add_node(productType.name)
    for processStep in PROCESS_STEPS:
        graph.add_node(processStep.name)
        graph.add_edge(processStep.name, processStep.machineType.name)
        graph.add_edge(processStep.name, processStep.toolType.name)
        graph.add_edge(processStep.name, processStep.consumesProductType.name)
        graph.add_edge(processStep.name, processStep.producesProductType.name)

    networkx.draw_networkx(graph)

    matplotlib.pyplot.show()

def toNetworkX():
    graph = networkx.Graph()

    for machineType in MACHINE_TYPES:
        graph.add_node(machineType.name)
    for toolType in TOOL_TYPES:
        graph.add_node(toolType.name)
    for productType in PRODUCT_TYPES:
        graph.add_node(productType.name)
    for processStep in PROCESS_STEPS:
        graph.add_node(processStep.name)
        graph.add_edge(processStep.name, processStep.machineType.name)
        graph.add_edge(processStep.name, processStep.toolType.name)
        graph.add_edge(processStep.name, processStep.consumesProductType.name)
        graph.add_edge(processStep.name, processStep.producesProductType.name)
    for scenario in SCENARIOS:
        graph.add_node(scenario.name)
    for customer in CUSTOMERS:
        graph.add_node(customer.name)
    for order in ORDERS:
        graph.add_node(f"Order {order.code}")
        graph.add_edge(f"Order {order.code}", order.productType.name)
        graph.add_edge(f"Order {order.code}", order.scenario.name)
        graph.add_edge(f"Order {order.code}", order.customer.name)
    for layout in LAYOUTS:
        graph.add_node(layout.name)
    for corridor in CORRIDORS:
        graph.add_node(f"Corridor {corridor.code}")
        graph.add_edge(f"Corridor {corridor.code}", corridor.layout.name)
    for machine in MACHINES:
        graph.add_node(machine.name)
        graph.add_edge(machine.name, machine.machineType.name)
        graph.add_edge(machine.name, f"Corridor {machine.corridor.code}")
    for simulation in SIMULATIONS:
        graph.add_node(f"Simulation {simulation.date}")
        graph.add_edge(f"Simulation {simulation.date}", simulation.scenario.name)
        graph.add_edge(f"Simulation {simulation.date}", simulation.layout.name)

    networkx.draw_networkx(graph)

    matplotlib.pyplot.show()

def toGraphML():
    graphml = '<graphml>'
    
    graphml += '</graphml>'

    return graphml