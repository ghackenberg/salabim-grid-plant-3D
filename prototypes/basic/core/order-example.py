# Data meta-model

class MachineType:
    instances = []
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size
        self.machineInstances: list[MachineInstance] = []
        self.operationTypes: list[OperationType] = []
        MachineType.instances.append(self)

class MachineInstance:
    instances = []
    def __init__(self, name: str, position: int, machineType: MachineType):
        self.name = name
        self.position = position
        self.machineType = machineType
        machineType.machineInstances.append(self)
        MachineInstance.instances.append(self)

class ToolType:
    instances = []
    def __init__(self, name: str):
        self.name = name
        self.operationTypes: list[OperationType] = []
        ToolType.instances.append(self)

class ObjectType:
    instances = []
    def __init__(self, name: str):
        self.name = name
        self.consumesOperationTypes: list[OperationType] = []
        self.producesOperationTypes: list[OperationType] = []
        self.orders: list[Order] = []
        ObjectType.instances.append(self)

class OperationType:
    instances = []
    def __init__(self, name: str, duration: int, machineType: MachineType, toolType: ToolType, consumes: ObjectType, produces: ObjectType):
        self.name = name
        self.duration = duration
        self.machineType = machineType
        self.toolType = toolType
        self.consumes = consumes
        self.produces = produces
        machineType.operationTypes.append(self)
        toolType.operationTypes.append(self)
        consumes.consumesOperationTypes.append(self)
        produces.producesOperationTypes.append(self)
        OperationType.instances.append(self)

class Scenario:
    instances = []
    def __init__(self, name: str):
        self.name = name
        self.orders: list[Order] = []
        Scenario.instances.append(self)

class Order:
    instances = []
    def __init__(self, date: str, amount: int, objectType: ObjectType, scenario: Scenario):
        self.date = date
        self.amount = amount
        self.objectType = objectType
        self.scenario = scenario
        objectType.orders.append(self)
        scenario.orders.append(self)
        Order.instances.append(self)

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

for instance in Scenario.instances:
    scenario: Scenario = instance

    with open(f"{scenario.name}.cfg", "w") as file:
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

        for instance in scenario.orders:
            order: Order = instance

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
