from .MachineType import MachineType
from .ToolType import ToolType
from .ObjectType import ObjectType

class OperationType:
    def __init__(self, name: str, machineType: MachineType, toolType: ToolType, consumesObjectType: ObjectType, producesObjectType: ObjectType) -> None:
        self.name = name
        self.machineType = machineType
        self.toolType = toolType
        self.consumesObjectType = consumesObjectType
        self.producesObjectType = producesObjectType

        machineType.operationTypes.append(self)
        toolType.operationTypes.append(self)
        consumesObjectType.consumingOperationTypes.append(self)
        producesObjectType.producingOperationTypes.append(self)

        OPERATION_TYPES.append(self)

OPERATION_TYPES: list[OperationType] = []