class Machine:

    """Representation of machines."""

    from ..Definition import MachineType
    
    from .Corridor import Corridor

    def __init__(self, name: str, machine_type: MachineType, corridor: Corridor, left: bool) -> None:

        # Remember properties
        self.name = name
        self.machine_type = machine_type
        self.corridor = corridor
        self.left = left

        # Remember relations
        machine_type.machines.append(self)  # appending machinetype to the list
        if left:
            corridor.machines_left.append(self)
        else:
            corridor.machines_right.append(self)

        # Remember instance
        MACHINES.append(self)

    def __repr__(self) -> str:

        return f"{self.name}"

MACHINES: list[Machine] = []
