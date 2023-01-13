from .MachineType import MachineType

class Machine:
    def __init__(self, name: str, machineType: MachineType) -> None:
        self.name = name
        self.machineType = machineType

        machineType.machines.append(self)

        MACHINES.append(self)

MACHINES: list[Machine] = []