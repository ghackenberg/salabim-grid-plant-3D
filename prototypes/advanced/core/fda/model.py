class MachineType:
    def __init__(self, name: str, code: int) -> None:
        # Remember properties
        self.name = name
        self.code = code
        # Remember relations
        self.machines: list[Machine] = []   #connection with machine class, define
        self.processSteps: list[ProcessStep] = []
        # Remember instance
        MACHINE_TYPES.append(self) #append the machinetype (itself) in the global list
    def __repr__(self) -> str:
        return f"{self.name}"

MACHINE_TYPES: list[MachineType] = [] #global list of possible machine types



class ToolType:
    def __init__(self, name: str, code: int, mountTime: int, unmountTime: int, totalLifeUnits: int) -> None:
        # Remember properties
        self.name = name
        self.code = code
        self.mountTime = mountTime
        self.unmountTime = unmountTime
        self.totalLifeUnits = totalLifeUnits
        # Remember relations
        self.processSteps: list[ProcessStep] = []
        # Remember instance
        TOOL_TYPES.append(self)
    def __repr__(self) -> str:
        return f"{self.name}"

TOOL_TYPES: list[ToolType] = []



class ProductType:
    def __init__(self, name: str, length: int, width: int, depth: int, weight: int) -> None:
        # Remember properties
        self.name = name
        self.length = length
        self.width = width
        self.depth = depth
        self.weight = weight
        # Remember relations
        self.consumingProcessSteps: list[ProcessStep] = []
        self.producingProcessSteps: list[ProcessStep] = []
        self.orders: list[Order] = []
        # Remember instance
        PRODUCT_TYPES.append(self)
    def __repr__(self) -> str:
        return f"{self.name}"

PRODUCT_TYPES: list[ProductType] = []



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
    def __init__(self, code: int, quantity: int, earliestStartDate: int, latestEndData: int, productType: ProductType, scenario: Scenario) -> None:
        # Remember properties
        self.code = code
        self.quantity = quantity
        self.earliestStartDate = earliestStartDate
        self.latestEndData = latestEndData
        self.productType = productType
        self.scenario = scenario
        # Remember relations
        productType.orders.append(self)
        scenario.orders.append(self)
        # Remember instance
        ORDERS.append(self)
    def __repr__(self) -> str:
        return f"{self.code}"

#it is not the customer order that contains the customers, but vice versa
ORDERS: list[Order] = []



class Layout:
    def __init__(self, name: str, storageTimeDeliver: int, storageTimeStore: int) -> None:
        # Remember properties
        self.name = name
        self.storageTimeDeliver = storageTimeDeliver
        self.storageTimeStore = storageTimeStore
        # Remember relations
        self.corridors: list[Corridor] = []
        # Remember instance
        LAYOUTS.append(self)
    def __repr__(self) -> str:
        return f"{self.name}"

LAYOUTS: list[Layout] = []



class ProcessStep:
    def __init__(self, name: str, duration: int, consumedToolLifeUnits: int, defectProbability: float, machineType: MachineType, toolType: ToolType, consumesProductType: ProductType, producesProductType: ProductType) -> None:
        # Remember properties
        self.name = name
        self.duration = duration
        self.consumedToolLifeUnits = consumedToolLifeUnits
        self.defectProbability = defectProbability
        self.machineType = machineType
        self.toolType = toolType
        self.consumesProductType = consumesProductType
        self.producesProductType = producesProductType
        # Remember relations
        machineType.processSteps.append(self)
        toolType.processSteps.append(self)
        consumesProductType.consumingProcessSteps.append(self)
        producesProductType.producingProcessSteps.append(self)
        # Remember instance
        PROCESS_STEPS.append(self)
    def __repr__(self) -> str:
        return f"{self.name}"

PROCESS_STEPS: list[ProcessStep] = []


class Corridor:
    def __init__(self, code: int, storageCapacity: int, storageTimeDeliver: int, storageTimeStore: int, layout: Layout) -> None:
        # Remember properties
        self.code = code
        self.storageCapacity = storageCapacity
        self.storageTimeDeliver = storageTimeDeliver
        self.storageTimeStore = storageTimeStore
        self.layout = layout
        # Remember relations
        layout.corridors.append(self)
        self.machinesLeft: list[Machine] = []
        self.machinesRight: list[Machine] = []
        # Remember instance
        CORRIDORS.append(self)

CORRIDORS: list[Corridor] = []


class Machine:
    def __init__(self, name: str, machineType: MachineType, corridor: Corridor, left: bool) -> None:
        # Remember properties
        self.name = name
        self.machineType = machineType
        self.corridor = corridor
        self.left = left
        # Remember relations
        machineType.machines.append(self)  #appending machinetype to the list
        if left:
            corridor.machinesLeft.append(self)
        else:
            corridor.machinesRight.append(self)
        # Remember instance
        MACHINES.append(self)
    def __repr__(self) -> str:
        return f"{self.name}"

MACHINES: list[Machine] = []