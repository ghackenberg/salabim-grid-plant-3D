from fda import *

# Layout parameters
NUM_CORRIDORS = 8

NUM_MACHINES_LEFT = 4
NUM_MACHINES_RIGHT = 4

# Create machine types
mt1 = MachineType('Machine type 1')

# Create tool types
tt1 = ToolType('Tool type 1', 2, 3, 10)
tt2 = ToolType('Tool type 2', 1, 2, 9)

# Create product types
pt1 = ProductType('Product type 1', 12, 12, 12, 5)
pt2 = ProductType('Product type 2', 12, 24, 11, 10)
pt3 = ProductType('Product type 3', 14, 15, 15, 6)

# Create process steps
o1 = Operation('Operation 1', 1, 5, 0.15, mt1, tt1, pt1, pt2)
o2 = Operation('Operation 2', 1, 4, 0.20, mt1, tt2, pt1, pt3)

# Create scenarios
scenario1 = Scenario('Scenario 1')

# Create orders
o1 = Order(1, 10, 11, 20, pt2, scenario1)
o2 = Order(2, 10, 11, 20, pt3, scenario1)

# Create layouts
l1 = Layout('Layout 1', 10, 5)

# Create corridors
for i in range(NUM_CORRIDORS):
    Corridor(f"Corridor {i + 1}", 200, 2, 3, l1)

# Create machines
for i in range(NUM_CORRIDORS):
    for j in range(NUM_MACHINES_LEFT):
        Machine(f'Machine 1.{i + 1}.{j + 1}.left', mt1, CORRIDORS[i], True)
    for j in range(NUM_MACHINES_RIGHT):
        Machine(f'Machine 1.{i + 1}.{j + 1}.right', mt1, CORRIDORS[i], False)

# Simulate
simulate(l1, scenario1, True)
