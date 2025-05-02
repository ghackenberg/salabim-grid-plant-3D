from SpineML import *

# Create machine types
mt1 = MachineType('Machine type 1')
mt2 = MachineType('Machine type 2')

# Create tool types
tt1 = ToolType('Tool type 1', 2, 3, 25)
tt2 = ToolType('Tool type 2', 1, 2, 25)

# Create product types
pt1 = ProductType('Product Type 1', 12, 12, 12, 5)
pt2 = ProductType('Product Type 2', 12, 24, 11, 10)
pt3 = ProductType('Product Type 3', 14, 15, 15, 6)

# Create process steps
OperationType('Operation 1', 1, 10, 0.15, mt1, tt1, pt1, pt2)
OperationType('Operation 2', 1, 10, 0.20, mt2, tt2, pt1, pt3)

# Create scenarios
s1 = Scenario('Scenario 1')

# Create orders
o1_1 = Order("Order 1.1", 5, 11, 20, pt2, s1)
o1_2 = Order("Order 1.2", 5, 11, 20, pt3, s1)

# Create layouts
l1 = Layout('Layout 1', 10, 5)

# Create corridors
c1_1 = Corridor("Corridor 1.1", 200, 2, 3, l1)

# Create machines
Machine('Machine 1.1.1', mt1, c1_1, True)
Machine('Machine 1.1.2', mt2, c1_1, False)

# Simulate
visualizeRoute(l1, o1_1)

simulate(l1, s1, True)
