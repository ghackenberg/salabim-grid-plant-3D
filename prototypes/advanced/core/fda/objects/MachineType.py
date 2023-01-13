from .Machine import Machine
from .OperationType import OperationType

class MachineType:
    def __init__(self, name: str) -> None:
        self.name = name

        self.machines: list[Machine] = []
        self.operationTypes: list[OperationType] = []

        MACINE_TYPES.append(self)

MACINE_TYPES: list[MachineType] = []