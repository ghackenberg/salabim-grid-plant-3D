class ToolType:

    """Representation of tool types."""

    def __init__(self, name: str, mount_time: int, unmount_time: int, total_life_units: int) -> None:

        from .OperationType import OperationType

        # Remember properties
        self.name = name
        self.mount_time = mount_time
        self.unmount_time = unmount_time
        self.total_life_units = total_life_units

        # Remember relations
        self.operations: list[OperationType] = []

        # Remember instance
        TOOL_TYPES.append(self)

    def __repr__(self) -> str:

        return f"{self.name}"

TOOL_TYPES: list[ToolType] = []
