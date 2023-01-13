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

orderA = Order("14.12.2022", 10, objectTypeC, scenarioA)
orderB = Order("15.12.2022", 30, objectTypeC, scenarioA)
orderC = Order("16.12.2022", 45, objectTypeC, scenarioA)

# Debug printing

print(orderA.scenario.name, orderA.date, orderA.amount, orderA.objectType.name)
print(orderB.scenario.name, orderB.date, orderB.amount, orderB.objectType.name)

print(objectTypeA.name, len(objectTypeA.producesOperationTypes))
print(objectTypeB.name, len(objectTypeB.producesOperationTypes), objectTypeB.producesOperationTypes[0].name)
print(objectTypeC.name, len(objectTypeC.producesOperationTypes), objectTypeC.producesOperationTypes[0].name)

with open("jaamsim_model.cfg", "w") as file:
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

    # ObjectTypes
    
    x = 0
    y = 0
    z = 0

    for instance in ObjectType.instances:
        objectType: ObjectType = instance
        
        name = objectType.name.replace(' ', '_').replace('.', '_').replace('(', '').replace(')', '')

        file.write(f"Define SimEntity {{ {name} }}\n")
        file.write(f"{name} Position {{ {x} {y} {z} m }}\n")

        y = y + 2
    
    # MachineInstances
    
    x = 4
    y = 0
    z = 0

    for instance in MachineInstance.instances:
        machineInstance: MachineInstance = instance

        name = machineInstance.name.replace(' ', '_').replace('.', '_').replace('(', '').replace(')', '')

        file.write(f"Define Queue {{ {name}_Queue_Before }}\n")
        file.write(f"{name}_Queue_Before Position {{ {x} {y} {z} m }}\n")

        file.write(f"Define Queue {{ {name}_Queue_After }}\n")
        file.write(f"{name}_Queue_After Position {{ {x + 4} {y} {z} m }}\n")

        file.write(f"Define Server {{ {name}_Server }}\n")
        file.write(f"{name}_Server Position {{ {x + 2} {y} {z} m }}\n")
        file.write(f"{name}_Server WaitQueue {{ {name}_Queue_Before }}\n")
        file.write(f"{name}_Server NextComponent {{ {name}_Queue_After }}\n")

        y = y + 2