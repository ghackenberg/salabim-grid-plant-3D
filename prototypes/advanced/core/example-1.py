from fda import *

# Create machine types
machineType1 = MachineType('Machine type 1')
machineType2 = MachineType('Machine type 2')
machineType3 = MachineType('Machine type 3')

# Create machines
machine1_1 = Machine('Machine 1.1', machineType1)
machine1_2 = Machine('Machine 1.2', machineType1)
machine1_3 = Machine('Machine 1.3', machineType1)

# Create tool types
toolType1 = ToolType('Tool type 1')
toolType2 = ToolType('Tool type 2')
toolType3 = ToolType('Tool type 3')

# Create object types
objectType1 = ObjectType('Object type 1')
objectType2 = ObjectType('Object type 2')
objectType3 = ObjectType('Object type 3')

# Create operation types
operationType1 = OperationType('Operation type 1', machineType1, toolType1, objectType1, objectType2)
operationType2 = OperationType('Operation type 2', machineType1, toolType2, objectType1, objectType3)
operationType3 = OperationType('Operation type 3', machineType2, toolType3, objectType1, objectType2)