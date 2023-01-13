class MachineType:
    def __init__(self, name: str) -> None:
        # Remember properties
        self.name = name
        # Remember relations
        self.machines: list[Machine] = []
        self.operationTypes: list[OperationType] = []
        # Remember instance
        MACHINE_TYPES.append(self)

MACHINE_TYPES: list[MachineType] = []

class Machine:
    def __init__(self, name: str, machineType: MachineType) -> None:
        # Remember properties
        self.name = name
        self.machineType = machineType
        # Remember relations
        machineType.machines.append(self)
        # Remember instance
        MACHINES.append(self)

MACHINES: list[Machine] = []

class ToolType:
    def __init__(self, name: str) -> None:
        # Remember properties
        self.name = name
        # Remember relations
        self.operationTypes: list[OperationType] = []
        # Remember instance
        TOOL_TYPES.append(self)

TOOL_TYPES: list[ToolType] = []

class ObjectType:
    def __init__(self, name: str) -> None:
        # Remember properties
        self.name = name
        # Remember relations
        self.consumingOperationTypes: list[OperationType] = []
        self.producingOperationTypes: list[OperationType] = []
        # Remember instance
        OBJECT_TYPES.append(self)

OBJECT_TYPES: list[ObjectType] = []

class OperationType:
    def __init__(self, name: str, machineType: MachineType, toolType: ToolType, consumesObjectType: ObjectType, producesObjectType: ObjectType) -> None:
        # Remember properties
        self.name = name
        self.machineType = machineType
        self.toolType = toolType
        self.consumesObjectType = consumesObjectType
        self.producesObjectType = producesObjectType
        # Remember relations
        machineType.operationTypes.append(self)
        toolType.operationTypes.append(self)
        consumesObjectType.consumingOperationTypes.append(self)
        producesObjectType.producingOperationTypes.append(self)
        # Remember instance
        OPERATION_TYPES.append(self)

OPERATION_TYPES: list[OperationType] = []