from fda import *


# Create machine types
machineType1 = MachineType('Machine type 1', 1)   # def __init__(self, name: str, code: int) -> None:
machineType2 = MachineType('Machine type 2', 2)
machineType3 = MachineType('Machine type 3', 3)


# Create tool types
toolType1 = ToolType('Tool type 1', 1, 2, 3, 10)
toolType2 = ToolType('Tool type 2', 2, 1, 2, 9)
toolType3 = ToolType('Tool type 3', 3, 3, 4, 12)


# Create Product Type
productType1 = ProductType('Product Type 1', 12, 12, 12, 5)
productType2 = ProductType('Product Type 2', 12, 24, 11, 10)
productType3 = ProductType('Product Type 3', 14, 15, 15, 6)
productType4 = ProductType('Product Type 4', 23, 11, 22, 5)


# Create Process Steps
processSteps1 = ProcessStep('Process 1', 20, 20, 0.15, machineType1, toolType1, productType1, productType2)
processSteps2 = ProcessStep('Process 2', 15, 24, 0.20, machineType2, toolType2, productType4, productType2)
processSteps3 = ProcessStep('Process 3', 10, 24, 0.11, machineType3, toolType3, productType1, productType4)


#Create Customer
customer1 = Customer('Rossi', 'Roma', 1)
customer2 = Customer('Alberti', 'Vienna', 2)


#Create Scenario
scenario1 = Scenario('Scenario 1')
scenario2 = Scenario('Scenario 2')


#Create CustomerOrder
order1 = Order(1, 10, 11, 20, productType1, customer1, scenario1)
order2 = Order(2, 5, 25, 30, productType2, customer2, scenario2)


#Create Layout
layout1= Layout('Layout 1', 200, 10, 5, 4)
layout2= Layout('Layout 2', 300, 11, 3, 3)


#Create T_Corridor
corridor1 = Corridor(1, 2, layout1)
corridor2 = Corridor(2, 1, layout2)


# Create machines
machine1_1 = Machine('Machine 1.1', machineType1, corridor1)
machine1_2 = Machine('Machine 1.2', machineType1, corridor1)
machine1_3 = Machine('Machine 1.3', machineType1, corridor1)
machine2_1 = Machine('Machine 2.1', machineType2, corridor2)
machine3_1 = Machine('Machine 3.1', machineType3, corridor2)


#Create Simulation
simulation1 = Simulation(1, layout1, scenario1)
simulation2 = Simulation(2, layout1, scenario2)


toNetworkX()


#for ProcessSteps in ProductType2.producingProcessSteps:
    #print(ProcessSteps.name + " can produce " + ProductType2.name)