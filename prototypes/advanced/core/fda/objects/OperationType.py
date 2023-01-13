from .MachineType import MachineType
from .ToolType import ToolType
from .ObjectType import ObjectType

class OperationType:
    def __init__(self, name: str, machineType: MachineType, toolType: ToolType, consumes: ObjectType, produces: ObjectType) -> None:
        self.name = name
        self.machineType = machineType
        self.toolType = toolType
        self.consumes = consumes
        self.produces = produces