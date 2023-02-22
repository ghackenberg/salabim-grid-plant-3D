from fda import *


# Create machine types
machineType1 = MachineType('Machine type 1', 1)
machineType2 = MachineType('Machine type 2', 2)
machineType3 = MachineType('Machine type 3', 3)
machineType4 = MachineType('Machine type 4', 4)


# Create tool types
toolType1 = ToolType('Tool type 1', 1, 2, 3, 10)
toolType2 = ToolType('Tool type 2', 2, 1, 2, 9)
toolType3 = ToolType('Tool type 3', 3, 3, 4, 12)


# Create Product Type
productType1 = ProductType('Product Type 1', 12, 12, 12, 5)
productType2 = ProductType('Product Type 2', 12, 24, 11, 10)
productType3 = ProductType('Product Type 3', 14, 15, 15, 6)
productType4 = ProductType('Product Type 4', 33, 12, 22, 17)


# Create Process Steps
processSteps1 = ProcessStep('Process 1', 20, 20, 0.15,machineType1, toolType1, productType1, productType2)
processSteps2 = ProcessStep('Process 2', 15, 24, 0.20, machineType2, toolType1, productType4, productType1)
processSteps3 = ProcessStep('Process 3', 10, 24, 0.11, machineType3, toolType3,productType3, productType4)
processSteps4 = ProcessStep('Process 3', 10, 24, 0.11, machineType4, toolType2,productType2, productType3)


# Create Customer
customer1 = Customer('Rossi', 'Roma', 1)
customer2 = Customer('Alberti', 'Vienna', 2)
customer3 = Customer('John', 'London', 3)


#Create Scenario
scenario1 = Scenario('Scenario 1')
scenario2 = Scenario('Scenario 2')
scenario3 = Scenario('Scenario 3')


# Create CustomerOrder
order1 = Order(1, 30, 11, 20, productType1, customer1, scenario1)
order2 = Order(2, 25, 25, 30, productType2, customer1, scenario1)
order3 = Order(3, 55, 11, 20, productType3, customer2, scenario2)
order4 = Order(4, 30, 25, 30, productType4, customer3, scenario3)


#Create Layout
layout1 = Layout('Layout 1', 200, 10, 5, 4)
layout2 = Layout('Layout 2', 300, 11, 3, 3)
layout3 = Layout('Layout 3', 150, 5, 1, 3)


#Create T_Corridor
corridor1_1 = Corridor(1, 2, layout1)
corridor1_2 = Corridor(1, 2, layout3)
corridor2 = Corridor(2, 1, layout1)
corridor3 = Corridor(3, 3, layout2)
corridor4 = Corridor(4, 2, layout3)


# Create machines
machine1_1 = Machine('Machine 1.1', machineType1, corridor1_1)
machine1_2 = Machine('Machine 1.2', machineType1, corridor1_1)
machine1_3 = Machine('Machine 1.3', machineType1, corridor1_1)
machine1_4 = Machine('Machine 1.1', machineType1, corridor1_2)
machine1_5 = Machine('Machine 1.2', machineType1, corridor1_2)
machine1_6 = Machine('Machine 1.3', machineType1, corridor1_2)
machine2_1 = Machine('Machine 2.1', machineType2, corridor2)
machine3_1 = Machine('Machine 3.1', machineType3, corridor3)
machine4_1 = Machine('Machine 4.1', machineType4, corridor4)


#Create Simulation
simulation1 = Simulation(1, layout1, scenario1)
simulation2 = Simulation(2, layout1, scenario2)
simulation3 = Simulation(3, layout1, scenario3)


toNetworkX()


#for ProcessSteps in ProductType2.producingProcessSteps:
    #print(ProcessSteps.name + " can produce " + ProductType2.name)


