import networkx
import matplotlib

from .model import *


def toNetworkXBasic():
    graph = networkx.DiGraph()

    node_color: list[str] = []

    for machineType in MACHINE_TYPES:
        graph.add_node(machineType.name)
        node_color.append("#ff0000")
    for toolType in TOOL_TYPES:
        graph.add_node(toolType.name)
        node_color.append("#00ff00")
    for productType in PRODUCT_TYPES:
        graph.add_node(productType.name)
        node_color.append("#0000ff")
    for processStep in PROCESS_STEPS:
        graph.add_node(processStep.name)
        graph.add_edge(processStep.machineType.name, processStep.name)
        graph.add_edge(processStep.toolType.name, processStep.name)
        graph.add_edge(processStep.consumesProductType.name, processStep.name)
        graph.add_edge(processStep.name, processStep.producesProductType.name)
        node_color.append("#ff00ff")

    networkx.draw_networkx(graph, arrows = True, node_color = node_color)

    matplotlib.pyplot.show()


def toNetworkXMinimal():
    graph = networkx.DiGraph()

    node_color: list[str] = []


    for productType in PRODUCT_TYPES:
        graph.add_node(productType.name)
        node_color.append("#0000ff")
    for processStep in PROCESS_STEPS:
        graph.add_node(processStep.name)

        graph.add_edge(processStep.consumesProductType.name, processStep.name)
        graph.add_edge(processStep.name, processStep.producesProductType.name)
        node_color.append("#ff00ff")

    networkx.draw_networkx(graph, arrows = True, node_color = node_color)

    matplotlib.pyplot.show()

def toNetworkX():
    graph = networkx.DiGraph()

    node_color: list[str] = []

    for machineType in MACHINE_TYPES:
        graph.add_node(machineType.name)
        node_color.append("#ff0000")
    for toolType in TOOL_TYPES:
        graph.add_node(toolType.name)
        node_color.append("#00ff00")
    for productType in PRODUCT_TYPES:
        graph.add_node(productType.name)
        node_color.append("#0000ff")
    for processStep in PROCESS_STEPS:
        graph.add_node(processStep.name)
        node_color.append("#880000")
        graph.add_edge(processStep.name, processStep.machineType.name)
        graph.add_edge(processStep.name, processStep.toolType.name)
        graph.add_edge(processStep.name, processStep.consumesProductType.name)
        graph.add_edge(processStep.name, processStep.producesProductType.name)
    for scenario in SCENARIOS:
        graph.add_node(scenario.name)
        node_color.append("#008800")
    for order in ORDERS:
        graph.add_node(f"Order {order.code}")
        node_color.append("#888800")
        graph.add_edge(f"Order {order.code}", order.productType.name)
        graph.add_edge(f"Order {order.code}", order.scenario.name)
    for layout in LAYOUTS:
        graph.add_node(layout.name)
        node_color.append("#008888")
    for corridor in CORRIDORS:
        graph.add_node(f"Corridor {corridor.code}")
        node_color.append("#880088")
        graph.add_edge(f"Corridor {corridor.code}", corridor.layout.name)
    for machine in MACHINES:
        graph.add_node(machine.name)
        node_color.append("#ffff00")
        graph.add_edge(machine.name, machine.machineType.name)
        graph.add_edge(machine.name, f"Corridor {machine.corridor.code}")

    networkx.draw_networkx(graph, arrows = True, node_color = node_color)

    matplotlib.pyplot.show()

def toGraphML():
    graphml = '<graphml>'
    
    graphml += '</graphml>'

    return graphml