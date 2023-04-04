from fda import *


# Create machine types
machineType1 = MachineType('Machine type 1', 1)


# Create tool types
toolType1 = ToolType('Tool type 1', 1, 2, 3, 10)
toolType2 = ToolType('Tool type 2', 2, 1, 2, 9)


# Create Product Type
productType1 = ProductType('Product Type 1', 12, 12, 12, 5)
productType2 = ProductType('Product Type 2', 12, 24, 11, 10)
productType3 = ProductType('Product Type 3', 14, 15, 15, 6)


# Create Process Steps
processSteps1 = ProcessStep('Process step 1', 1, 20, 0.15, machineType1, toolType1, productType1, productType2)
processSteps2 = ProcessStep('Process step 2', 1, 24, 0.20, machineType1, toolType2, productType1, productType3)


#Create Scenario
scenario1 = Scenario('Scenario 1')


#Create CustomerOrder
order1 = Order(1, 10, 11, 20, productType2,  scenario1)
order2 = Order(2, 10, 11, 20, productType3,  scenario1)


#Create Layout
layout1= Layout('Layout 1', 10, 5)


#Create T_Corridor
corridor1 = Corridor(1, 200, 2, 3, layout1)


# Create machines
machine1 = Machine('Machine 1', machineType1, corridor1, True)
machine2 = Machine('Machine 2', machineType1, corridor1, False)


# Simulate
simulate(layout1, scenario1)