from fda import *


# Create machine types
machineType1 = MachineType('Machine type 1', 1)
machineType2 = MachineType('Machine type 2', 2)
machineType3 = MachineType('Machine type 3', 3)
machineType4 = MachineType('Machine type 4', 4)

# Create tool types
toolType1 = ToolType('Tool type 1', 1, 2, 3, 20)
toolType2 = ToolType('Tool type 2', 2, 1, 2, 9)
toolType3 = ToolType('Tool type 3', 3, 3, 4, 12)


# Create product types
productType1 = ProductType('Product Type 1', 12, 12, 12, 5)
productType2 = ProductType('Product Type 2', 12, 24, 11, 10)
productType3 = ProductType('Product Type 3', 14, 15, 15, 6)
productType4 = ProductType('Product Type 4', 23, 11, 22, 5)


# Create process steps
processSteps1 = Operation('Process 1', 1, 10, 0.15, machineType1, toolType1, productType1, productType2)
processSteps2 = Operation('Process 2', 1, 4, 0.20, machineType2, toolType2, productType4, productType2)
processSteps3 = Operation('Process 3', 1, 4, 0.11, machineType3, toolType3, productType1, productType4)
processSteps4 = Operation('Process 4', 1, 3, 0.11, machineType4, toolType3, productType3, productType1)
processSteps4_2 = Operation('Process 4_2', 1,5, 0.11, machineType4, toolType2, productType3, productType1)


# Create scenarios
scenario1 = Scenario('Scenario 1') #Best Case
scenario2 = Scenario('Scenario 2') #Middle Case
scenario3 = Scenario('Scenario 3') #Worst Case


# Create orders
order1 = Order(1, 2, 11, 30, productType2,  scenario1)
order1_2 = Order(1, 3, 15, 30, productType1,  scenario1)
order2 = Order(2, 10, 20, 30, productType2,  scenario2)
order3 = Order(3, 10, 11, 12, productType4,  scenario3)
order4 = Order(4, 10, 25, 26, productType1,  scenario3)


# Create layouts
layout1 = Layout('Layout 1', 10, 5)
layout2 = Layout('Layout 2', 11, 3)
layout3 = Layout('Layout 3', 5, 1)


# Create corridors
corridor1_1 = Corridor(1, 200, 2, 3, layout1)
corridor1_2 = Corridor(2, 300, 2, 3, layout1)
corridor1_3 = Corridor(3, 150, 2, 3, layout1)
corridor2_1 = Corridor(4, 150, 2, 3, layout2)
corridor2_2 = Corridor(5, 150, 2, 3, layout2)
corridor3_1 = Corridor(6, 200, 2, 3, layout3)
corridor3_2 = Corridor(7, 150, 2, 3, layout3)
corridor3_3 = Corridor(8, 130, 2, 3, layout3)


# Create machines
machine1_1 = Machine('Machine 1.1', machineType1, corridor1_2, True)
machine1_2 = Machine('Machine 1.2', machineType1, corridor1_3, False)
machine1_3 = Machine('Machine 1.3', machineType1, corridor3_3, True)
machine1_4 = Machine('Machine 1.4', machineType1, corridor3_2, True)

machine2_1 = Machine('Machine 2.1', machineType2, corridor1_1, True)
machine2_2 = Machine('Machine 2.2', machineType2, corridor3_3, True)
machine2_3 = Machine('Machine 2.3', machineType2, corridor3_2, False)

machine3_1 = Machine('Machine 3.1', machineType3, corridor1_1, False)
machine3_2 = Machine('Machine 3.2', machineType3, corridor1_2, False)
machine3_3 = Machine('Machine 3.3', machineType3, corridor2_1, True)
machine3_4 = Machine('Machine 3.4', machineType3, corridor3_2, True)
machine3_5 = Machine('Machine 3.5', machineType3, corridor3_1, False)
machine3_6 = Machine('Machine 3.6', machineType3, corridor3_1, True)

machine4_1 = Machine('Machine 4.1', machineType4, corridor1_1, True)
machine4_2 = Machine('Machine 4.2', machineType4, corridor2_2, False)
machine4_3 = Machine('Machine 4.3', machineType4, corridor3_1, False)
machine4_4 = Machine('Machine 4.4', machineType4, corridor3_2, False)


# Simulate
simulate(layout3, scenario1, False)