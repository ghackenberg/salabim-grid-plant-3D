# Data meta-model

class MachineType:
    def __init__(self, name: str):
        self.name = name
        self.machineInstances: list[MachineInstance] = []
        self.operationTypes: list[OperationType] = []
        MACHINE_TYPES.append(self)
MACHINE_TYPES: list[MachineType] = []

class ToolType:
    def __init__(self, name: str):
        self.name = name
        self.operationTypes: list[OperationType] = []
        TOOL_TYPES.append(self)
TOOL_TYPES: list[ToolType] = []

class ObjectType:
    def __init__(self, name: str):
        self.name = name
        self.consumesOperationTypes: list[OperationType] = []
        self.producesOperationTypes: list[OperationType] = []
        self.orders: list[Order] = []
        OBJECT_TYPES.append(self)
    def __repr__(self) -> str:
        return f"{self.name}"
OBJECT_TYPES: list[ObjectType] = []

class MachineInstance:
    def __init__(self, name: str, machineType: MachineType):
        self.name = name
        self.machineType = machineType
        machineType.machineInstances.append(self)
        MACHINE_INSTANCES.append(self)
MACHINE_INSTANCES: list[MachineInstance] = []

class OperationType:
    def __init__(self, name: str, duration: int, machineType: MachineType, toolType: ToolType, consumes: ObjectType, produces: ObjectType):
        self.name = name
        self.duration = duration
        self.machineType = machineType
        self.toolType = toolType
        self.consumes = consumes
        self.produces = produces
        machineType.operationTypes.append(self)
        toolType.operationTypes.append(self)
        consumes.consumesOperationTypes.append(self)
        produces.producesOperationTypes.append(self)
        OPERATION_TYPES.append(self)
    def __repr__(self) -> str:
        return f"{self.name}"
OPERATION_TYPES: list[OperationType] = []

class Scenario:
    def __init__(self, name: str):
        self.name = name
        self.orders: list[Order] = []
        SCENARIOS.append(self)
SCENARIOS: list[Scenario] = []

class Order:
    def __init__(self, date: str, amount: int, objectType: ObjectType, scenario: Scenario):
        self.date = date
        self.amount = amount
        self.objectType = objectType
        self.scenario = scenario
        objectType.orders.append(self)
        scenario.orders.append(self)
        ORDERS.append(self)
ORDERS: list[Order] = []

# Algorithms

def calculateProcesses(objectType: ObjectType):
    result: list[list[OperationType]] = []
    for operationType in objectType.producesOperationTypes:
        prefixes = calculateProcesses(operationType.consumes)
        if not prefixes:
            result.append([operationType])
        else:
            for prefix in prefixes:
                prefix.append(operationType)
                result.append(prefix)
    return result

def calculateSources(objectType: ObjectType):
    chains = calculateProcesses(objectType)
    result: list[ObjectType] = []
    for chain in chains:
        if not chain[0].consumes in result:
            result.append(chain[0].consumes)
    return result

# Data model

machineTypeA = MachineType("DMG MORI Work Center X")
machineTypeB = MachineType("DMG MORI Work Center Y")

toolTypeA = ToolType("Driller")
toolTypeB = ToolType("Grinder")

objectTypeA = ObjectType("Metal Disk")
objectTypeB = ObjectType("Metal Gear (Raw)")
objectTypeC = ObjectType("Metal Gear (Finished)")

machineInstanceA = MachineInstance("DMG MORI Work Center X.1", machineTypeA)
machineInstanceA = MachineInstance("DMG MORI Work Center X.2", machineTypeA)
machineInstanceB = MachineInstance("DMG MORI Work Center Y.1", machineTypeB)
machineInstanceA = MachineInstance("DMG MORI Work Center X.3", machineTypeA)
machineInstanceA = MachineInstance("DMG MORI Work Center X.4", machineTypeA)
machineInstanceB = MachineInstance("DMG MORI Work Center Y.2", machineTypeB)

operationTypeA = OperationType("Produce raw gear from disk", 1, machineTypeA, toolTypeA, objectTypeA, objectTypeB)
operationTypeB = OperationType("Produce finished gear from raw gear", 1, machineTypeB, toolTypeB, objectTypeB, objectTypeC)
operationTypeC = OperationType("Produce finished gear from disk", 5, machineTypeB, toolTypeB, objectTypeA, objectTypeC)

scenarioA = Scenario("Best Case")
scenarioB = Scenario("Worst Case")
scenarioC = Scenario("Average Case")

orderA = Order("0 d", 10, objectTypeC, scenarioA)
orderB = Order("0 d", 30, objectTypeC, scenarioA)
orderC = Order("0 d", 45, objectTypeC, scenarioA)
orderD = Order("0 d", 10, objectTypeB, scenarioA)
orderE = Order("0 d", 30, objectTypeB, scenarioA)
orderF = Order("0 d", 45, objectTypeB, scenarioA)

print(calculateProcesses(objectTypeC))
print(calculateSources(objectTypeC))

for scenario in SCENARIOS:

    with open(f"{scenario.name}.cfg", "w") as file:



        # Simulation
        file.write("Simulation RealTime { TRUE }\n")
        file.write("Simulation SnapToGrid { TRUE }\n")
        file.write("Simulation ShowLabels { TRUE }\n")
        file.write("Simulation ShowSubModels { TRUE }\n")
        file.write("Simulation ShowEntityFlow { TRUE }\n")
        file.write("Simulation ShowModelBuilder { TRUE }\n")
        file.write("Simulation ShowObjectSelector { TRUE }\n")
        file.write("Simulation ShowInputEditor { TRUE }\n")
        file.write("Simulation ShowOutputViewer { TRUE }\n")
        file.write("Simulation ShowPropertyViewer { FALSE }\n")
        file.write("Simulation ShowLogViewer { FALSE }\n")

        # DefaultView
        file.write("Define View { DefaultView }\n")
        file.write("DefaultView ShowWindow { TRUE }\n")

        # View
        file.write("DefaultView Lock2D { TRUE }\n")
        file.write("DefaultView ViewCenter { 20  10  20  m }\n")
        file.write("DefaultView ViewPosition { 6  5  60  m }\n")



        ##########
        # BLOCKS #
        ##########



        # ROBOT BLOCKS
        file.write(f"Define EntityContainer {{ GR }}\n")
        file.write(f"Define EntityGenerator {{ Order_Generator_GR }}\n")

        # START BLOCKS
        file.write(f"Define Queue {{ Stock_1 }}\n")
        file.write(f"Define Branch {{ Direction_0 }}\n")
        file.write(f"Define EntityConveyor {{ Production_line_0}}\n")
        file.write(f"Define EntityConveyor {{ Production_line_back_0}}\n")
        file.write(f"Define Queue {{ ContainerQueue_0 }}\n")
        file.write(f"Define AddTo {{ Add_0 }}\n")
        file.write(f"Define EntityConveyor {{ Parallel_2_0 }}\n")
        file.write(f"Define EntityConveyor {{ Parallel_1_0 }}\n")

        # MACHINE INSTANCE BLOCKS
        x = 0
        y = 0

        count = 1

        for machineInstance in MACHINE_INSTANCES:

            file.write(f"Define EntityConveyor {{ Parallel_2_{count} }}\n")
            file.write(f"Define EntityConveyor {{ Parallel_1_{count} }}\n")
            file.write(f"Define Queue {{ ContainerQueue_{count} }}\n")
            file.write(f"Define EntityConveyor {{ Production_line_back_{count} }}\n")
            file.write(f"Define Branch {{ Direction_{count} }}\n")
            file.write(f"Define EntityConveyor {{ Production_line_{count} }}\n")
            file.write(f"Define AddTo {{ Add_{count} }}\n")
            file.write(f"Define Queue {{ Queue_B_M_{count} }}\n")
            file.write(f"Define Queue {{ Queue_A_M_{count} }}\n")
            file.write(f"Define ExpressionThreshold {{ Machine_Controller_{count} }}\n")
            file.write(f"Define ExpressionThreshold {{ Remove_Controller_{count} }}\n")
            file.write(f"Define ExpressionThreshold {{ Back_Controller_{count} }}\n")
            file.write(f"Define ExpressionThreshold {{ Add_Controller_{count} }}\n")
            file.write(f"Define RemoveFrom {{ Remove_{count} }}\n")
            file.write(f"Define Server {{ Machine_{count} }}\n")

            count = count + 1

        # END BLOCKS
        file.write(f"Define Queue {{ FinalQueue }}\n") 
        file.write(f"Define EntityConveyor {{ Final_line}}\n")
        file.write(f"Define Branch {{ Direction_{count} }}\n") 
        file.write(f"Define EntityConveyor {{ Final_line_back }}\n")
        file.write(f"Define EntitySink {{ Customer }}\n")
        file.write(f"Define RemoveFrom {{ Last_Remove }}\n")



        ##############
        # PARAMETERS #
        ##############



        # ROBOT PARAMETERS

        # ROBOT PARAMETERS - Container GR
        file.write(f"GR Position {{ -11 {y + 20} 0 m }}\n")

        # ROBOT PARAMETERS - Generator for GR
        file.write(f"Order_Generator_GR NextComponent {{ Direction_0 }}\n")
        file.write(f"Order_Generator_GR PrototypeEntity {{ GR }}\n")
        file.write(f"Order_Generator_GR FirstArrivalTime {{ 0 s }}\n")
        file.write(f"Order_Generator_GR EntitiesPerArrival {{ 1 }}\n")
        file.write(f"Order_Generator_GR MaxNumber {{ 1 }}\n")
        file.write(f"Order_Generator_GR Position {{ -8 {y + 20} 0 m }}\n")



        # START PARAMETERS

        # START PARAMETERS - Initial Station Block
                
        # START PARAMETERS - ContainerQueue
        file.write(f"ContainerQueue_0 Position {{ {x - 6} {y + 14} 0 m }}\n")

        # START PARAMETERS - conveyor back
        file.write(f"Production_line_back_0 NextComponent {{ ContainerQueue_0 }}\n")
        file.write(f"Production_line_back_0 Position {{ {x - 7} {y + 15} 0 m }}\n")
        file.write(f"Production_line_back_0 Points {{ {{ {x - 7} {y + 18} 0 m }} {{ {x - 7} {y + 15} 0  m }} }}\n") 
        file.write(f"Production_line_back_0 TravelTime {{ 35 s }}\n")                   

        # START PARAMETERS - branch
        file.write(f"Direction_0 Position {{ {x - 5} {y + 20} 0 m }}\n")
        file.write(f"Direction_0 NextComponentList {{ Production_line_back_0 Parallel_1_0 }}\n")
        file.write(f"Direction_0 Choice {{ 'this.obj.Count == 0 ? 1 : 2' }}\n")
        
        # START PARAMETERS - DownLine
        file.write(f"Parallel_2_0 NextComponent {{ Direction_0 }}\n")
        file.write(f"Parallel_2_0 Position {{ {x - 1} {y + 19} 0 m }}\n")
        file.write(f"Parallel_2_0 Points {{ {{ {x + 1} {y + 19} 0 m }} {{ {x - 1} {y + 19} 0  m }} }}\n") 
        file.write(f"Parallel_2_0 TravelTime {{ 35 s }}\n")

        # START PARAMETERS - UpLine functions    
        file.write(f"Parallel_1_0 NextComponent {{ Direction_1 }}\n")
        file.write(f"Parallel_1_0 Position {{ {x - 1} {y + 21} 0 m }}\n")
        file.write(f"Parallel_1_0 Points {{ {{ {x - 1} {y + 21} 0 m }} {{ {x + 1} {y + 21} 0  m }} }}\n") 
        file.write(f"Parallel_1_0 TravelTime {{ 35 s }}\n")

        # START PARAMETERS - conveyor PL
        file.write(f"Production_line_0 NextComponent {{ Direction_0 }}\n")
        file.write(f"Production_line_0 Position {{ {x - 3} {y + 15} 0 m }}\n")
        file.write(f"Production_line_0 Points {{ {{ {x - 3} {y + 15} 0 m }} {{ {x - 3} {y + 18} 0  m }} }}\n") 
        file.write(f"Production_line_0 TravelTime {{ 35 s }}\n")

        # START PARAMETERS - AddTo
        file.write(f"Add_0 Position {{ {x - 3} {y + 12} 0 m }}\n")
        file.write(f"Add_0 NextComponent {{ Production_line_0 }}\n")           
        file.write(f"Add_0 ContainerQueue {{ ContainerQueue_0 }}\n")
        file.write(f"Add_0 WaitQueue {{ Stock_1 }}\n")

        # START PARAMETERS - Stock parameter
        file.write(f"Stock_1 Position {{ -3 8 0 m }}\n")
        file.write(f"Stock_1 MaxPerLine {{ 5 }}\n")
        file.write(f"Stock_1 MaxRows {{ 5 }}\n")



        # MACHINE INSTANCE PARAMETERS

        x = 0
        y = 0

        count = 1

        for machineInstance in MACHINE_INSTANCES:
        
            #ContainerQueue
            file.write(f"ContainerQueue_{count} Position {{ {x + 4} {y + 14} 0 m }}\n")

            #conveyor back
            file.write(f"Production_line_back_{count} NextComponent {{ ContainerQueue_{count} }}\n")
            file.write(f"Production_line_back_{count} Position {{ {x + 3} {y + 15} 0 m }}\n")
            file.write(f"Production_line_back_{count} Points {{ {{ {x + 3} {y + 18} 0 m }} {{ {x + 3} {y + 15} 0  m }} }}\n") 
            file.write(f"Production_line_back_{count} TravelTime {{ 35 s }}\n")                   

            #branch
            file.write(f"Direction_{count} Position {{ {x + 5} {y + 20} 0 m }}\n")
            file.write(f"Direction_{count} NextComponentList {{ Production_line_back_{count} Parallel_1_{count} Parallel_2_{count - 1} }}\n")
            file.write(f"Direction_{count} Choice {{ '")
            file.write(f"(this.obj.Count == 0) ? (")
            file.write(f"   ([Back_Controller_{count}].Open) ? (")
            file.write(f"       3")
            file.write(f"   ) : (")
            file.write(f"       1")
            file.write(f"   )")
            file.write(f") : (")
            file.write(f"   (this.obj.obj.State == this.obj.obj.FinalState) ? (")
            file.write(f"       2")
            file.write(f"   ) : (")
            file.write(f'       (size(this.obj.obj.StateMachineOperationTypes(this.obj.obj.State)("{machineInstance.name}"))) ? (')
            file.write(f"           1")
            file.write(f"       ) : (")
            file.write(f"           2")
            file.write(f"       )")
            file.write(f"   )")
            file.write(f")")
            file.write(f"' }}\n")
            
            #DownLine
            file.write(f"Parallel_2_{count} NextComponent {{ Direction_{count} }}\n")
            file.write(f"Parallel_2_{count} Position {{ {x + 9} {y + 19} 0 m }}\n")
            file.write(f"Parallel_2_{count} Points {{ {{ {x + 11} {y + 19} 0 m }} {{ {x + 9} {y + 19} 0  m }} }}\n") 
            file.write(f"Parallel_2_{count} TravelTime {{ 35 s }}\n")

            #UpLine
            file.write(f"Parallel_1_{count} NextComponent {{ Direction_{count + 1} }}\n")
            file.write(f"Parallel_1_{count} Position {{ {x + 9} {y + 21} 0 m }}\n")
            file.write(f"Parallel_1_{count} Points {{ {{ {x + 9} {y + 21} 0 m }} {{ {x + 11} {y + 21} 0  m }} }}\n") 
            file.write(f"Parallel_1_{count} TravelTime {{ 35 s }}\n")

            #conveyor PL
            file.write(f"Production_line_{count} NextComponent {{ Direction_{count} }}\n")
            file.write(f"Production_line_{count} Position {{ {x + 7} {y + 15} 0 m }}\n")
            file.write(f"Production_line_{count} Points {{ {{ {x + 7} {y + 15} 0 m }} {{ {x + 7} {y + 18} 0  m }} }}\n") 
            file.write(f"Production_line_{count} TravelTime {{ 35 s }}\n")

            #AddTo
            file.write(f"Add_{count} Position {{ {x + 7} {y + 12} 0 m }}\n")
            file.write(f"Add_{count} NextComponent {{ Production_line_{count} }}\n")            
            file.write(f"Add_{count} ContainerQueue {{ ContainerQueue_{count} }}\n")

            #Queue before machine
            file.write(f"Queue_B_M_{count} Position {{ {x + 4} {y + 10} 0 m }}\n")

            #Queue after machine
            file.write(f"Queue_A_M_{count} Position {{ {x + 7} {y + 10} 0 m }}\n")

            #Threshold Machine
            file.write(f"Machine_Controller_{count} Position {{ {x + 7} {y + 6} 0 m }}\n")
            file.write(f"Machine_Controller_{count} OpenCondition {{'[Production_line_{count}].NumberInProgress == 0'}}\n")

            #Threshold Remove
            file.write(f"Remove_Controller_{count} Position {{ {x + 2} {y + 12} 0 m }}\n")
            file.write(f"Remove_Controller_{count} OpenCondition {{'[Queue_A_M_{count}].QueueLength == 0'}}\n")

            #Threshold Backward 
            file.write(f"Back_Controller_{count} Position {{ {x + 2} {y + 15} 0 m }}\n")
            file.write(f"Back_Controller_{count} OpenCondition {{ '[Queue_B_M_{count}].QueueLength + [Machine_{count}].NumberInProgress == 0' }}\n")

            #Threshold Add
            file.write(f"Add_Controller_{count} Position {{ {x + 9} {y + 12} 0 m }}\n")
            file.write(f"Add_Controller_{count} OpenCondition {{'[Queue_A_M_{count}].QueueLength == 1 || [Add_{count}].NumberInProgress == 1'}}\n")

            #Remove
            file.write(f"Remove_{count} Position {{ {x + 4} {y + 12} 0 m }}\n")
            file.write(f"Remove_{count} NextForContainers {{ Production_line_{count} }}\n")
            file.write(f"Remove_{count} NextComponent {{ Queue_B_M_{count} }}\n")
            file.write(f"Remove_{count} WaitQueue {{ ContainerQueue_{count} }}\n")
            file.write(f"Remove_{count} ImmediateThresholdList {{ Remove_Controller_{count} }}\n")

            #Machine
            file.write(f"Machine_{count} Position {{ {x + 7} {y + 8} 0 m }}\n")
            file.write(f"Machine_{count} NextComponent {{ Queue_A_M_{count} }}\n")
            file.write(f"Machine_{count} WaitQueue {{ Queue_B_M_{count} }}\n")
            file.write(f"Machine_{count} ServiceTime {{ 30 s }}\n")
            file.write(f"Machine_{count} StateAssignment {{ 'this.obj.FinalState' }}\n")
            file.write(f"Machine_{count} ImmediateThresholdList {{ Machine_Controller_{count} }}\n")
            operationTypes = ''
            for operationType in machineInstance.machineType.operationTypes:
                if operationTypes:
                    operationTypes = f'{operationTypes}, "{operationType.name}"'
                else:
                    operationTypes = f'"{operationType.name}"'
            file.write(f"Machine_{count} AttributeDefinitionList {{ OperationTypes '{{ {operationTypes} }}' }}\n")

            #Add Connections
            file.write(f"Add_{count} WaitQueue {{ Queue_A_M_{count} }}\n")
            file.write(f"Add_{count} ImmediateThresholdList {{ Add_Controller_{count} }}\n")

            #Production Line Back Connection
            file.write(f"Production_line_back_{count} ImmediateThresholdList {{ Back_Controller_{count} }}\n")
  
            count = count + 1

            x = x + 10



        # END PARAMETERS
                    
        # END PARAMETERS - ContainerQueue
        file.write(f"FinalQueue Position {{ {x + 4} 12 0 m }}\n")

        # END PARAMETERS - conveyor PL
        file.write(f"Final_line NextComponent {{ FinalQueue }}\n")
        file.write(f"Final_line Position {{ {x + 4} 18 0 m }}\n")
        file.write(f"Final_line Points {{ {{ {x + 4} 18 0 m }} {{ {x + 4} 15 0  m }} }}\n")
        file.write(f"Final_line TravelTime {{ 35 s }}\n")  

        # END PARAMETERS - branch
        file.write(f"Direction_{count} Position {{ {x + 5} 20 0 m }}\n")
        file.write(f"Direction_{count} NextComponentList {{ Final_line Parallel_2_{count - 1} }}\n")
        file.write(f"Direction_{count} Choice {{ '(this.obj.Count == 0) ? (2) : ((this.obj.obj.State == this.obj.obj.FinalState) ? (1) : (2))' }}\n")

        # END PARAMETERS - conveyor back
        file.write(f"Final_line_back NextComponent {{ Direction_{count} }}\n")
        file.write(f"Final_line_back Position {{ {x + 6} 15 0 m }}\n")
        file.write(f"Final_line_back Points {{ {{ {x + 6} 15 0 m }} {{ {x + 6} 18 0  m }} }}\n") 
        file.write(f"Final_line_back TravelTime {{ 35 s }}\n")                   
                
        # END PARAMETERS - Customer Sink
        file.write(f"Customer Position {{ {x + 6} 8 0 m }}\n")

        # END PARAMETERS - Remove
        file.write(f"Last_Remove Position {{ {x + 6} 12 0 m }}\n")
        file.write(f"Last_Remove NextForContainers {{ Final_line_back}}\n")
        file.write(f"Last_Remove NextComponent {{ Customer }}\n")
        file.write(f"Last_Remove WaitQueue {{ FinalQueue }}\n")



        # ORDER PARAMETERS

        x = 0
        y = 0

        count = 1

        for order in scenario.orders:

            processes = calculateProcesses(order.objectType)

            # Calcualte mapping between states, machines, and operations
            stateMachineOperationTypes: dict[str, dict[str, list[str]]] = {}
            for process in processes:
                for operationType in process:
                    objectTypeName = operationType.consumes.name
                    if not objectTypeName in stateMachineOperationTypes:
                        stateMachineOperationTypes[objectTypeName] = {}
                    for machineInstance in operationType.machineType.machineInstances:
                        if not machineInstance.name in stateMachineOperationTypes[objectTypeName]:
                            stateMachineOperationTypes[objectTypeName][machineInstance.name] = []
                        stateMachineOperationTypes[objectTypeName][machineInstance.name].append(operationType.name)
            
            # Translate data structure to JaamSim scripting language
            stateMachineOperationTypesExpr = f'{{'
            states = 0
            for objectType in OBJECT_TYPES:
                separator = ', ' if states else ''
                stateMachineOperationTypesExpr = f'{stateMachineOperationTypesExpr}{separator}"{objectType.name}"={{'
                machineInstances = 0
                for machineInstance in MACHINE_INSTANCES:
                    separator = ', ' if machineInstances else ''
                    stateMachineOperationTypesExpr = f'{stateMachineOperationTypesExpr}{separator}"{machineInstance.name}"={{'
                    if objectType.name in stateMachineOperationTypes and machineInstance.name in stateMachineOperationTypes[objectType.name]:
                        operationTypes = 0
                        for operationTypeName in stateMachineOperationTypes[objectType.name][machineInstance.name]:
                            separator = ', ' if operationTypes else ''
                            stateMachineOperationTypesExpr = f'{stateMachineOperationTypesExpr}{separator}"{operationTypeName}"'
                            operationTypes = operationTypes + 1
                    stateMachineOperationTypesExpr = f'{stateMachineOperationTypesExpr}}}'
                    machineInstances = machineInstances + 1
                stateMachineOperationTypesExpr = f'{stateMachineOperationTypesExpr}}}'
                states = states + 1
            stateMachineOperationTypesExpr = f"{stateMachineOperationTypesExpr}}}"

            # Calculate initial state
            source = processes[0][0].consumes

            file.write(f"Define SimEntity {{ Order_Prototype_{count} }}\n")
            file.write(f"Order_Prototype_{count} AttributeDefinitionList {{ {{ FinalState '\"{order.objectType.name}\"' }} {{ StateMachineOperationTypes '{stateMachineOperationTypesExpr}' }} }}\n")
            #set initial state as raw
            file.write(f"Order_Prototype_{count} InitialState {{ '{source.name}' }}\n")
            file.write(f"Order_Prototype_{count} Position {{ {x - 12} 0 0 m }}\n")

            file.write(f"Define EntityGenerator {{ Order_Generator_{count} }}\n")
            file.write(f"Order_Generator_{count} PrototypeEntity {{ Order_Prototype_{count} }}\n")
            file.write(f"Order_Generator_{count} NextComponent {{ Stock_1 }}\n")
            file.write(f"Order_Generator_{count} FirstArrivalTime {{ {order.date} }}\n")
            file.write(f"Order_Generator_{count} EntitiesPerArrival {{ {order.amount} }}\n")
            file.write(f"Order_Generator_{count} MaxNumber {{ {order.amount} }}\n")
            file.write(f"Order_Generator_{count} Position {{ {x - 12} 3 0 m }}\n")

            count = count + 1

            x = x + 3