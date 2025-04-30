import networkx
import matplotlib.pyplot as plt

from .model import MACHINE_TYPES, TOOL_TYPES, PRODUCT_TYPES, OPERATIONS, SCENARIOS, ORDERS, LAYOUTS, CORRIDORS, MACHINES

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
    for processStep in OPERATIONS:
        graph.add_node(processStep.name)
        graph.add_edge(processStep.machine_type.name, processStep.name)
        graph.add_edge(processStep.tool_type.name, processStep.name)
        graph.add_edge(processStep.consumes_product_type.name, processStep.name)
        graph.add_edge(processStep.name, processStep.produces_product_type.name)
        node_color.append("#ff00ff")

    networkx.draw_networkx(graph, arrows = True, node_color = node_color)

    plt.show()

def toNetworkXMinimal():
    graph = networkx.DiGraph()

    node_color: list[str] = []


    for productType in PRODUCT_TYPES:
        graph.add_node(productType.name)
        node_color.append("#0000ff")
    for processStep in OPERATIONS:
        graph.add_node(processStep.name)

        graph.add_edge(processStep.consumes_product_type.name, processStep.name)
        graph.add_edge(processStep.name, processStep.produces_product_type.name)
        node_color.append("#ff00ff")

    networkx.draw_networkx(graph, arrows = True, node_color = node_color)

    plt.show()

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
    for processStep in OPERATIONS:
        graph.add_node(processStep.name)
        node_color.append("#880000")
        graph.add_edge(processStep.name, processStep.machine_type.name)
        graph.add_edge(processStep.name, processStep.tool_type.name)
        graph.add_edge(processStep.name, processStep.consumes_product_type.name)
        graph.add_edge(processStep.name, processStep.produces_product_type.name)
    for scenario in SCENARIOS:
        graph.add_node(scenario.name)
        node_color.append("#008800")
    for order in ORDERS:
        graph.add_node(f"Order {order.code}")
        node_color.append("#888800")
        graph.add_edge(f"Order {order.code}", order.product_type.name)
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
        graph.add_edge(machine.name, machine.machine_type.name)
        graph.add_edge(machine.name, f"Corridor {machine.corridor.code}")

    networkx.draw_networkx(graph, arrows = True, node_color = node_color)

    plt.show()