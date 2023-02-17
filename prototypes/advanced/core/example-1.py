from fda import *

# Create machine types
machineType1 = MachineType('Machine type 1', 1)   # def __init__(self, name: str, code: int) -> None:
machineType2 = MachineType('Machine type 2', 2)
machineType3 = MachineType('Machine type 3', 3)


# Create tool types
toolType1 = ToolType('Tool type 1', 1, 2, 3, 10)
toolType2 = ToolType('Tool type 2', 2, 1, 2, 9)
toolType3 = ToolType('Tool type 3', 3, 3, 4, 12)


#Create Customer
Customer1 = Customer('Rossi', 'Roma', 1)
Customer2 = Customer('Alberti', 'Vienna', 2)


#Create Simulation
Simulation1 = Simulation(1)
Simulation2 = Simulation(2)


#Create Scenario
Scenario1 = Scenario('Scenario 1', Simulation1)
Scenario2 = Scenario('Scenario 2', Simulation2)


#Create CustomerOrder
CustomerOrder1 = CustomerOrder(1, 10, 11, 20, Customer1, Scenario1)
CustomerOrder2 = CustomerOrder(2, 5, 25, 30, Customer2, Scenario2)


# Create Product Type
ProductType1 = ProductType('Product Type 1', 12, 12, 12, 5, CustomerOrder1)
ProductType2 = ProductType('Product Type 2', 12, 24, 11, 10, CustomerOrder1)
ProductType3 = ProductType('Product Type 3', 14, 15, 15, 6, CustomerOrder2)
ProductType4 = ProductType('Product Type 4', 23, 11, 22, 5, CustomerOrder2)


# Create Process Steps
ProcessSteps1 = ProcessSteps('Process 1', 20, 20, 0.15, machineType1, toolType1, ProductType1, ProductType2)
ProcessSteps2 = ProcessSteps('Process 2', 15, 24, 0.20, machineType2, toolType2, ProductType4, ProductType2)
ProcessSteps3 = ProcessSteps('Process 3', 10, 24, 0.11, machineType3, toolType3, ProductType1, ProductType4)


#Create Layout
Layout1= Layout('Layout 1', 200, 10, 5, 4, Simulation1)
Layout2= Layout('Layout 2', 300, 11, 3, 3, Simulation2)


#Create T_Corridor
T_Corridor1 = T_Corridor(1, 2, Layout1)
T_Corridor2 = T_Corridor(2, 1, Layout2)


# Create machines
machine1_1 = Machine('Machine 1.1', machineType1, T_Corridor1)
machine1_2 = Machine('Machine 1.2', machineType1, T_Corridor1)
machine1_3 = Machine('Machine 1.3', machineType1, T_Corridor1)
machine2_1 = Machine('Machine 2.1', machineType2, T_Corridor2)
machine3_1 = Machine('Machine 3.1', machineType3, T_Corridor2)




#for ProcessSteps in ProductType2.producingProcessSteps:
    #print(ProcessSteps.name + " can produce " + ProductType2.name)


