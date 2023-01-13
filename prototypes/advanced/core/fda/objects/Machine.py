from .MachineType import MachineType

class Machine:
    def __init__(self, name: str, type: MachineType) -> None:
        self.name = name
        self.type = type