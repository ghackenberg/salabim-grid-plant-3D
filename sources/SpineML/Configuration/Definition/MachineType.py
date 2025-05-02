class MachineType:

    """Representation of machine types."""

    from .ToolType import ToolType

    def __init__(self, name: str) -> None:

        from .OperationType import OperationType
        
        from ..Solution import Machine

        # Remember properties
        self.name = name

        # Remember relations
        self.machines: list[Machine] = []
        self.operations: list[OperationType] = []

        # Remember instance
        MACHINE_TYPES.append(self)  # append the machinetype (itself) in the global list

    def __repr__(self) -> str:

        return f"{self.name}"

    def computeToolTypes(self) -> list[ToolType]:

        """Compute tool types for this machine type from operation types."""

        from .ToolType import ToolType

        tool_types: list[ToolType] = []
        for process_step in self.operations:
            if process_step.tool_type not in tool_types:
                tool_types.append(process_step.tool_type)
        return tool_types
    
MACHINE_TYPES: list[MachineType] = []
