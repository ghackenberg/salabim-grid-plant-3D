from fda import *


# Create machine types
machineType1 = MachineType('Machine type 1', 1)
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
productType4 = ProductType('Product Type 4', 33, 12, 22, 17)


# Create Process Steps
processSteps1 = ProcessStep('Process 1', 20, 20, 0.15,machineType1, toolType1, productType1, productType2)
processSteps2 = ProcessStep('Process 2', 15, 24, 0.20, machineType2, toolType2, productType4, productType1)
processSteps3 = ProcessStep('Process 3', 10, 24, 0.11, machineType3, toolType3,productType3, productType4)


#Create Scenario
scenario1 = Scenario('Scenario 1') #Best Case
scenario2 = Scenario('Scenario 2') #Worst Case


#Create CustomerOrder
order1 = Order(1, 10, 11, 20, productType1,  scenario1)
order2 = Order(2, 500, 25, 26, productType2,  scenario2)
order3 = Order(3, 400, 14, 16, productType2, scenario2)



#Create Layout
layout1= Layout('Layout 1', 10, 5) #Best Case
layout2= Layout('Layout 2', 11, 7)#Middle Case
layout3= Layout('Layout 3', 11, 3) #Worst Case


#Create T_Corridor
corridor1 = Corridor(1, 200, layout1)
corridor2 = Corridor(2,150, layout1)
corridor3 = Corridor(3, 300, layout2)
corridor4 = Corridor(4, 200, layout2)
corridor4_1 = Corridor(4, 200, layout3)
corridor5 = Corridor(3, 300, layout3)
corridor6 = Corridor(4, 200, layout3)

# Create machines
machine3_1 = Machine('Machine 3.1', machineType3, corridor1)
machine3_2 = Machine('Machine 3.2', machineType3, corridor2)
machine3_3 = Machine('Machine 3.3', machineType3, corridor3)
machine3_4 = Machine('Machine 3.4', machineType3, corridor5)
machine2_1 = Machine('Machine 2.1', machineType2, corridor1)
machine2_2 = Machine('Machine 2.2', machineType2, corridor2)
machine2_3 = Machine('Machine 2.3', machineType2, corridor3)
machine2_4 = Machine ('Machine 2.4', machineType2, corridor6)
machine1_1 = Machine('Machine 1.1', machineType1, corridor1)
machine1_2 = Machine('Machine 1.2', machineType1, corridor2)
machine1_3 = Machine('Machine1.3', machineType1, corridor4)
machine1_4 = Machine('Machine1.4', machineType1, corridor4_1)


#Create Simulation
simulation1 = Simulation(1, layout1, scenario1)
simulation2 = Simulation(2, layout2, scenario2)
simualtion3 = Simulation(3, layout3, scenario2)


toNetworkXMinimal()


#for ProcessSteps in ProductType2.producingProcessSteps:
    #print(ProcessSteps.name + " can produce " + ProductType2.name)