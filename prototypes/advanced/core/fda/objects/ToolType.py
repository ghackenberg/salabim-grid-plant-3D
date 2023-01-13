from .OperationType import OperationType

class ToolType:
    def __init__(self, name: str) -> None:
        self.name = name

        self.operationTypes: list[OperationType] = []

        TOOL_TYPES.append(self)

TOOL_TYPES: list[ToolType] = []