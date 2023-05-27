from fda import *

# Create machine types
mt1 = MachineType('Machine type 1')
mt2 = MachineType('Machine type 2')
mt3 = MachineType('Machine type 3')
mt4 = MachineType('Machine type 4')

# Create tool types
tt1 = ToolType('Tool type 1', 2, 3, 20)
tt2 = ToolType('Tool type 2', 1, 2, 9)
tt3 = ToolType('Tool type 3', 3, 4, 12)

# Create product types
pt1 = ProductType('Product Type 1', 12, 12, 12, 5)
pt2 = ProductType('Product Type 2', 12, 24, 11, 10)
pt3 = ProductType('Product Type 3', 14, 15, 15, 6)
pt4 = ProductType('Product Type 4', 23, 11, 22, 5)

# Create process steps
Operation('Operation 1', 1, 10, 0.15, mt1, tt1, pt1, pt2)
Operation('Operation 2', 1, 4, 0.20, mt2, tt2, pt4, pt2)
Operation('Operation 3', 1, 4, 0.11, mt3, tt3, pt1, pt4)
Operation('Operation 4', 1, 3, 0.11, mt4, tt3, pt3, pt1)
Operation('Operation 5', 1, 5, 0.11, mt4, tt2, pt3, pt1)

# Create scenarios
s1 = Scenario('Scenario 1')
s2 = Scenario('Scenario 2')
s3 = Scenario('Scenario 3')

# Create orders
# ... scenario 1
Order("Order 1.1", 2, 11, 30, pt2, s1)
Order("Order 1.2", 3, 15, 30, pt1, s1)
# ... scenario 2
Order("Order 2.1", 10, 20, 30, pt2, s2)
# ... scenario 3
Order("Order 3.1", 10, 11, 12, pt4, s3)
Order("Order 3.2", 10, 25, 26, pt1, s3)

# Create layouts
l1 = Layout('Layout 1', 10, 5)
l2 = Layout('Layout 2', 11, 3)
l3 = Layout('Layout 3', 5, 1)

# Create corridors

# ... layout 1
c1_1 = Corridor("Corridor 1.1", 200, 2, 3, l1)
c1_2 = Corridor("Corridor 1.2", 300, 2, 3, l1)
c1_3 = Corridor("Corridor 1.3", 150, 2, 3, l1)
# ... layout 2
c2_1 = Corridor("Corridor 2.1", 150, 2, 3, l2)
c2_2 = Corridor("Corridor 2.2", 150, 2, 3, l2)
# ... layout 3
c3_1 = Corridor("Corridor 3.1", 200, 2, 3, l3)
c3_2 = Corridor("Corridor 3.2", 150, 2, 3, l3)
c3_3 = Corridor("Corridor 3.3", 130, 2, 3, l3)

# Create machines

# ... layout 1 / corridor 1
Machine('Machine 1.1.1', mt2, c1_1, True)
Machine('Machine 1.1.2', mt4, c1_1, True)
Machine('Machine 1.1.3', mt3, c1_1, False)
# ... layout 1 / corridor 2
Machine('Machine 1.2.1', mt1, c1_2, True)
Machine('Machine 1.2.2', mt3, c1_2, False)
# ... layout 1 / corridor 3
Machine('Machine 1.3.1', mt1, c1_3, False)

# ... layout 2 / corridor 1
Machine('Machine 2.1.1', mt3, c2_1, True)
# ... layout 2 / corridor 2
Machine('Machine 2.2.1', mt4, c2_2, False)

# ... layout 3 / corridor 1
Machine('Machine 3.1.1', mt3, c3_1, True)
Machine('Machine 3.1.2', mt3, c3_1, False)
Machine('Machine 3.1.3', mt4, c3_1, False)
# ... layout 3 / corridor 2
Machine('Machine 3.2.1', mt1, c3_2, True)
Machine('Machine 3.2.2', mt3, c3_2, True)
Machine('Machine 3.2.3', mt2, c3_2, False)
Machine('Machine 3.2.4', mt4, c3_2, False)
# ... layout 3 / corridor 3
Machine('Machine 3.3.1', mt1, c3_3, True)
Machine('Machine 3.3.2', mt2, c3_3, True)

# Simulate
simulate(l3, s1)
