from fda import *


# Create machine types
machineType1 = MachineType('Machine type 1', 1)
machineType2 = MachineType('Machine type 2', 2)
machineType3 = MachineType('Machine type 3', 3)


# Create tool types
toolType1 = ToolType('Tool type 1', 1, 2, 3, 10)
toolType2 = ToolType('Tool type 2', 2, 1, 2, 9)
toolType3 = ToolType('Tool type 3', 3, 3, 4, 12)


# Create product types
productType1 = ProductType('Product Type 1', 12, 12, 12, 5)
productType2 = ProductType('Product Type 2', 12, 24, 11, 10)
productType3 = ProductType('Product Type 3', 14, 15, 15, 6)
productType4 = ProductType('Product Type 4', 33, 12, 22, 17)


# Create process steps
processSteps1 = ProcessStep('Process 1', 1, 5, 0.15,machineType1, toolType1, productType1, productType2)
processSteps2 = ProcessStep('Process 2', 1, 4, 0.20, machineType2, toolType2, productType4, productType1)
processSteps3 = ProcessStep('Process 3', 1, 6, 0.11, machineType3, toolType3,productType3, productType4)


# Create scenarios
scenario1 = Scenario('Scenario 1') #Best Case
scenario2 = Scenario('Scenario 2') #Worst Case


# Create orders
order1 = Order(1, 10, 11, 20, productType1,  scenario1)
order2 = Order(2, 500, 25, 26, productType2,  scenario2)
order3 = Order(3, 400, 14, 16, productType2, scenario2)


# Create layouts
layout1= Layout('Layout 1', 10, 5) #Best Case
layout2= Layout('Layout 2', 11, 7)#Middle Case
layout3= Layout('Layout 3', 11, 3) #Worst Case


# Create corridors
corridor1_1 = Corridor(1, 200, 3, 4, layout1)
corridor1_2 = Corridor(2, 150, 1, 2, layout1)
corridor2_1 = Corridor(3, 300, 2, 3, layout2)
corridor2_2 = Corridor(4, 200, 1, 1, layout2)
corridor3_1 = Corridor(4, 200, 1, 1, layout3)
corridor3_2 = Corridor(3, 300, 1, 1, layout3)
corridor3_3 = Corridor(4, 200, 1, 1, layout3)


# Create machines
machine3_1 = Machine('Machine 3.1', machineType3, corridor1_1, True)
machine3_2 = Machine('Machine 3.2', machineType3, corridor1_2, True)
machine3_3 = Machine('Machine 3.3', machineType3, corridor2_1, True)
machine3_4 = Machine('Machine 3.4', machineType3, corridor3_2, True)
machine2_1 = Machine('Machine 2.1', machineType2, corridor1_1, True)
machine2_2 = Machine('Machine 2.2', machineType2, corridor1_2, True)
machine2_3 = Machine('Machine 2.3', machineType2, corridor2_1, True)
machine2_4 = Machine ('Machine 2.4', machineType2, corridor3_3, True)
machine1_1 = Machine('Machine 1.1', machineType1, corridor1_1, False)
machine1_2 = Machine('Machine 1.2', machineType1, corridor1_2, False)
machine1_3 = Machine('Machine1.3', machineType1, corridor2_2, True)
machine1_4 = Machine('Machine1.4', machineType1, corridor3_1, True)


# Simulate
simulate(layout1, scenario1)