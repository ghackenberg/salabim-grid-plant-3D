class ToolType:
    def __init__(self, name: str, code: int, mount_time: int, unmount_time: int, total_life_units: int) -> None:
        # Remember properties
        self.name = name
        self.code = code
        self.mount_time = mount_time
        self.unmount_time = unmount_time
        self.total_life_units = total_life_units
        # Remember relations
        self.operations: list[Operation] = []
        # Remember instance
        TOOL_TYPES.append(self)
    def __repr__(self) -> str:
        return f"{self.name}"

TOOL_TYPES: list[ToolType] = []


class MachineType:
    def __init__(self, name: str, code: int) -> None:
        # Remember properties
        self.name = name
        self.code = code
        # Remember relations
        self.machines: list[Machine] = []   #connection with machine class, define
        self.operations: list[Operation] = []
        # Remember instance
        MACHINE_TYPES.append(self) #append the machinetype (itself) in the global list

    def __repr__(self) -> str:
        return f"{self.name}"
    
    def computeToolTypes(self) -> list[ToolType]:
        tool_types: list[ToolType] = []
        for process_step in self.operations:
            if process_step.tool_type not in tool_types:
                tool_types.append(process_step.tool_type)
        return tool_types

MACHINE_TYPES: list[MachineType] = [] #global list of possible machine types


class ProductType:
    def __init__(self, name: str, length: int, width: int, depth: int, weight: int) -> None:
        # Remember properties
        self.name = name
        self.length = length
        self.width = width
        self.depth = depth
        self.weight = weight
        # Remember relations
        self.consuming_operations: list[Operation] = []
        self.producing_operations: list[Operation] = []
        self.orders: list[Order] = []
        # Remember instance
        PRODUCT_TYPES.append(self)
    def __repr__(self) -> str:
        return f"{self.name}"

PRODUCT_TYPES: list[ProductType] = []


class Operation:
    def __init__(self, name: str, duration: int, consumes_life_units: int, defect_probability: float, machine_type: MachineType, tool_type: ToolType, consumes_product_type: ProductType, produces_product_type: ProductType) -> None:
        # Remember properties
        self.name = name
        self.duration = duration
        self.consumes_life_units = consumes_life_units
        self.defect_probability = defect_probability
        self.machine_type = machine_type
        self.tool_type = tool_type
        self.consumes_product_type = consumes_product_type
        self.produces_product_type = produces_product_type
        # Remember relations
        machine_type.operations.append(self)
        tool_type.operations.append(self)
        consumes_product_type.consuming_operations.append(self)
        produces_product_type.producing_operations.append(self)
        # Remember instance
        OPERATIONS.append(self)

    def __repr__(self) -> str:
        return f"{self.name}"

OPERATIONS: list[Operation] = []


class Scenario:
    def __init__(self, name: str) -> None:
        # Remember properties
        self.name = name
        # Remember relations, scenario: Scenario
        self.orders: list[Order] = []
        # Remember instance
        SCENARIOS.append(self)
    def __repr__(self) -> str:
        return f"{self.name}"

#the scenario class contains the specifications of the customer orders.
SCENARIOS: list[Scenario] = []    #I consider this list in case the user wants to keep the data of different scenario tested


class Order:
    def __init__(self, code: int, quantity: int, earliest_start_time: int, latest_end_time: int, product_type: ProductType, scenario: Scenario) -> None:
        # Remember properties
        self.code = code
        self.quantity = quantity
        self.earliest_start_time = earliest_start_time
        self.latest_end_time = latest_end_time
        self.product_type = product_type
        self.scenario = scenario
        # Remember relations
        product_type.orders.append(self)
        scenario.orders.append(self)
        # Remember instance
        ORDERS.append(self)
    def __repr__(self) -> str:
        return f"{self.code}"

#it is not the customer order that contains the customers, but vice versa
ORDERS: list[Order] = []


class Layout:
    def __init__(self, name: str, storage_out_time: int, storage_in_time: int) -> None:
        # Remember properties
        self.name = name
        self.storage_out_time = storage_out_time
        self.storage_in_time = storage_in_time
        # Remember relations
        self.corridors: list[Corridor] = []
        # Remember instance
        LAYOUTS.append(self)
    def __repr__(self) -> str:
        return f"{self.name}"

LAYOUTS: list[Layout] = []


class Corridor:
    def __init__(self, code: int, storage_capacity: int, storage_out_time: int, storage_in_type: int, layout: Layout) -> None:
        # Remember properties
        self.code = code
        self.storage_capacity = storage_capacity
        self.storage_out_time = storage_out_time
        self.storage_in_time = storage_in_type
        self.layout = layout
        # Remember relations
        layout.corridors.append(self)
        self.machines_left: list[Machine] = []
        self.machines_right: list[Machine] = []
        # Remember instance
        CORRIDORS.append(self)

CORRIDORS: list[Corridor] = []


class Machine:
    def __init__(self, name: str, machine_type: MachineType, corridor: Corridor, left: bool) -> None:
        # Remember properties
        self.name = name
        self.machine_type = machine_type
        self.corridor = corridor
        self.left = left
        # Remember relations
        machine_type.machines.append(self)  #appending machinetype to the list
        if left:
            corridor.machines_left.append(self)
        else:
            corridor.machines_right.append(self)
        # Remember instance
        MACHINES.append(self)
    def __repr__(self) -> str:
        return f"{self.name}"

MACHINES: list[Machine] = []