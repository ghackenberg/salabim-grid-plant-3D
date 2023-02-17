# Data meta-model

class MachineType:
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size
        self.machineInstances: list[MachineInstance] = []
        self.operationTypes: list[OperationType] = []
        MACHINE_TYPES.append(self)

MACHINE_TYPES: list[MachineType] = []

class MachineInstance:
    def __init__(self, name: str, position: int, machineType: MachineType):
        self.name = name
        self.position = position
        self.machineType = machineType
        machineType.machineInstances.append(self)
        MACHINE_INSTANCES.append(self)

MACHINE_INSTANCES: list[MachineInstance] = []

class ToolType:
    def __init__(self, name: str):
        self.name = name
        self.operationTypes: list[OperationType] = []
        TOOL_TYPES.append(self)

TOOL_TYPES: list[ToolType] = []

class ObjectType:
    def __init__(self, name: str):
        self.name = name
        self.consumesOperationTypes: list[OperationType] = []
        self.producesOperationTypes: list[OperationType] = []
        self.orders: list[Order] = []
        OBJECT_TYPES.append(self)

OBJECT_TYPES: list[ObjectType] = []

class OperationType:
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
        OPERATION_TYPES.append(self)

OPERATION_TYPES: list[OperationType] = []

class Scenario:
    def __init__(self, name: str):
        self.name = name
        self.orders: list[Order] = []
        SCENARIOS.append(self)

SCENARIOS: list[Scenario] = []

class Order:
    def __init__(self, date: str, amount: int, objectType: ObjectType, scenario: Scenario):
        self.date = date
        self.amount = amount
        self.objectType = objectType
        self.scenario = scenario
        objectType.orders.append(self)
        scenario.orders.append(self)
        ORDERS.append(self)

ORDERS: list[Order] = []