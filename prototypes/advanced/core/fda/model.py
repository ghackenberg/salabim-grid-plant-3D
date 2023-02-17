class MachineType:
    def __init__(self, name: str, code: int) -> None:
        # Remember properties
        self.name = name
        self.code = code
        # Remember relations
        self.machines: list[Machine] = []   #connection with machine class, define
        self.processSteps: list[ProcessSteps] = []
        # Remember instance
        MACHINE_TYPES.append(self) #append the machinetype (itself) in the global list

MACHINE_TYPES: list[MachineType] = [] #global list of possible machine types




class ToolType:
    def __init__(self, name: str, code: int, mountTime: int, unmountTime: int, totalLifeUnits: int) -> None:
        # Remember properties
        self.name = name
        self.mountTime = mountTime
        self.unmountTime = unmountTime
        self.code = code
        self.totalLifeUnits = totalLifeUnits
        # Remember relations
        self.processSteps: list[ProcessSteps] = []
        # Remember instance
        TOOL_TYPES.append(self)

TOOL_TYPES: list[ToolType] = []





class Customer:
    def __init__(self, name: str, location: str, orderPriority: int) -> None:
        # Remember properties
        self.name = name
        self.location = location
        self.orderPriority = orderPriority
        # Remember relations
        self.customerorder: list[CustomerOrder] = []
        # Remember instance
        CUSTOMERS.append(self)

CUSTOMERS: list[Customer] = []



class Simulation:
    def __init__(self, date: int) -> None:
        # Remember properties
        self.date = date
        # Remember relations
        self.layout: list[Layout] = []
        self.scenario: list[Scenario] = []

        # Remember instance
        SIMULATIONS.append(self)
#the simulation class contains the info related to the layout and the scenario to visualize.

SIMULATIONS: list[Simulation] = []  # I consider this list in case the user wants to keep the data of different simulation run


class Scenario:
    def __init__(self, name: str, simulation: Simulation) -> None:
        # Remember properties
        self.name = name
        self.simulation = simulation
        # Remember relations, scenario: Scenario

        simulation.scenario.append(self)
        self.customerorder: list[CustomerOrder] = []
        # Remember instance
        SCENARIOS.append(self)
#the scenario class contains the specifications of the customer orders.
SCENARIOS: list[Scenario] = []    #I consider this list in case the user wants to keep the data of different scenario tested


class CustomerOrder:
    def __init__(self, OrderCode: int, quantity: int, EarliestStartDate: int, LatestEndData: int, customer: Customer, scenario: Scenario) -> None:
        # Remember properties
        self.OrderCode = OrderCode
        self.quantity = quantity
        self.EarliestStartDate = EarliestStartDate
        self.LatestEndData = LatestEndData
        self.scenario = scenario
        # Remember relations
        customer.customerorder.append(self)
        scenario.customerorder.append(self)
        self.productType: list[ProductType] = []

        # Remember instance
        CUSTOMER_ORDERS.append(self)
#it is not the customer order that contains the customers, but vice versa
CUSTOMER_ORDERS: list[CustomerOrder] = []


class ProductType:
    def __init__(self, name: str, length: int, width: int, depth: int, weight: int, customerorder: CustomerOrder) -> None:
        # Remember properties
        self.name = name
        self.length = length
        self.width = width
        self.depth = depth
        self.weight = weight
        # Remember relations
        self.consumingProcessSteps: list[ProcessSteps] = []
        self.producingProcessSteps: list[ProcessSteps] = []
        customerorder.productType.append(self)
        # Remember instance
        PRODUCT_TYPES.append(self)

PRODUCT_TYPES: list[ProductType] = []



class ProcessSteps:
    def __init__(self, name: str, duration: int, ConsumedToolLifeUnits: int, defectProbability: float, machineType: MachineType, toolType: ToolType, consumesProductType: ProductType, producesProductType: ProductType) -> None:
        # Remember properties
        self.name = name
        self.machineType = machineType
        self.toolType = toolType
        self.consumesProductType = consumesProductType
        self.producesProductType = producesProductType
        self.ConsumedToolLifeUnits = ConsumedToolLifeUnits
        self.duration = duration
        self.defectProbability = defectProbability
        # Remember relations
        machineType.processSteps.append(self)
        toolType.processSteps.append(self)
        consumesProductType.consumingProcessSteps.append(self)
        producesProductType.producingProcessSteps.append(self)
        # Remember instance
        PROCESS_STEPS.append(self)

PROCESS_STEPS: list[ProcessSteps] = []


class Layout:
    def __init__(self, name: str, StorageCapacity: int, StorageTime_Deliver: int, StorageTime_Store: int, NumRobots_MainCorridor: int, simulation: Simulation) -> None:
        # Remember properties
        self.name = name
        self.StorageCapacity = StorageCapacity
        self.StorageTime_Deliver = StorageTime_Deliver
        self.StorageTime_Store = StorageTime_Store
        self.NumRobots_MainCorridor = NumRobots_MainCorridor
        self.simulation= simulation
        # Remember relations

        self.t_corridor: list[T_Corridor] = []
        simulation.layout.append(self)
        # Remember instance
        LAYOUTS.append(self)


LAYOUTS: list[Layout] = []


class T_Corridor:
    def __init__(self, code: int, robots: int, layout: Layout) -> None:
        # Remember properties
        self.code = code
        self.robots = robots
        self.layout = layout
        # Remember relations
        layout.t_corridor.append(self)
        self.machines: list[Machine] = []

        # Remember instance
        CORRIDORS.append(self)

CORRIDORS: list[T_Corridor] = []


class Machine:
    def __init__(self, name: str, machineType: MachineType, t_corridor: T_Corridor) -> None:
        # Remember properties
        self.name = name
        self.machineType = machineType
        self.t_corridor = t_corridor
        # Remember relations
        machineType.machines.append(self)  #appending machinetype to the list
        t_corridor.machines.append(self)

        # Remember instance
        MACHINES.append(self)

MACHINES: list[Machine] = []





