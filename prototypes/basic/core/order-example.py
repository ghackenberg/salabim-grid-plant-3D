from fda import *

# Data model

machineTypeA = MachineType("DMG MORI Work Center X", 10)
machineTypeB = MachineType("DMG MORI Work Center Y", 10)

machineInstanceA = MachineInstance("DMG MORI Work Center X.1", 2, machineTypeA)
machineInstanceB = MachineInstance("DMG MORI Work Center X.2", 4, machineTypeA)
machineInstanceC = MachineInstance("DMG MORI Work Center X.3", 6, machineTypeA)
machineInstanceD = MachineInstance("DMG MORI Work Center Y.1", 8, machineTypeB)
machineInstanceE = MachineInstance("DMG MORI Work Center Y.2", 10, machineTypeB)

toolTypeA = ToolType("Driller")
toolTypeB = ToolType("Grinder")

objectTypeA = ObjectType("Metal Disk")
objectTypeB = ObjectType("Metal Gear (Raw)")
objectTypeC = ObjectType("Metal Gear (Finished)")
objectTypeD = ObjectType("Wooden Disk")
objectTypeE = ObjectType("Wooden Gear (Raw)")
objectTypeF = ObjectType("Wooden Gear (Finished)")

operationTypeA = OperationType("Produce raw gear from disk", 1, machineTypeA, toolTypeA, objectTypeA, objectTypeB)
operationTypeB = OperationType("Produce finished gear from raw gear", 1, machineTypeB, toolTypeB, objectTypeB, objectTypeC)

scenarioA = Scenario("Best Case")
scenarioB = Scenario("Worst Case")
scenarioC = Scenario("Average Case")

orderA = Order("1 d", 10, objectTypeC, scenarioA)
orderB = Order("2 d", 30, objectTypeC, scenarioA)
orderC = Order("3 d", 45, objectTypeC, scenarioA)
orderD = Order("4 d", 10, objectTypeB, scenarioA)
orderE = Order("5 d", 30, objectTypeB, scenarioA)
orderF = Order("6 d", 45, objectTypeA, scenarioA)

for scenario in SCENARIOS:

    with open(f"order-example {scenario.name}.cfg", "w") as file:
        # Simulation

        file.write("Simulation RealTime { TRUE }\n")
        file.write("Simulation SnapToGrid { TRUE }\n")
        file.write("Simulation ShowLabels { TRUE }\n")
        file.write("Simulation ShowSubModels { TRUE }\n")
        file.write("Simulation ShowEntityFlow { TRUE }\n")
        file.write("Simulation ShowModelBuilder { TRUE }\n")
        file.write("Simulation ShowObjectSelector { TRUE }\n")
        file.write("Simulation ShowInputEditor { TRUE }\n")
        file.write("Simulation ShowOutputViewer { TRUE }\n")
        file.write("Simulation ShowPropertyViewer { FALSE }\n")
        file.write("Simulation ShowLogViewer { FALSE }\n")

        # DefaultView

        file.write("Define View { DefaultView }\n")
        file.write("DefaultView ShowWindow { TRUE }\n")

        # Orders

        file.write(f"Define Queue {{ Order_Queue }}\n")
        file.write(f"Order_Queue Position {{ 0 3 0 m }}\n")
        file.write(f"Order_Queue MaxPerLine {{ 5 }}\n")
        file.write(f"Order_Queue MaxRows {{ 5 }}\n")

        count = 0

        for order in scenario.orders:

            file.write(f"Define SimEntity {{ Order_Prototype_{count} }}\n")
            file.write(f"Order_Prototype_{count} AttributeDefinitionList {{ {{ Type '\"{order.objectType.name}\"' }} }}\n")
            file.write(f"Order_Prototype_{count} Position {{ {count * 3} -3 0 m }}\n")

            file.write(f"Define EntityGenerator {{ Order_Generator_{count} }}\n")
            file.write(f"Order_Generator_{count} PrototypeEntity {{ Order_Prototype_{count} }}\n")
            file.write(f"Order_Generator_{count} NextComponent {{ Order_Queue }}\n")
            file.write(f"Order_Generator_{count} FirstArrivalTime {{ {order.date} }}\n")
            file.write(f"Order_Generator_{count} EntitiesPerArrival {{ {order.amount} }}\n")
            file.write(f"Order_Generator_{count} MaxNumber {{ {order.amount} }}\n")
            file.write(f"Order_Generator_{count} Position {{ {count * 3} 0 0 m }}\n")

            count = count + 1
