from .Configuration import ProductType, OperationType, Layout, Machine

def calculateMachineSequencesFromOperationSequence(process: list[OperationType], layout: Layout) -> list[list[Machine]]:
    if len(process) > 0:
        result: list[list[Machine]] = []
        processStep = process.pop(0)
        for machine in processStep.machine_type.machines:
            if machine.corridor.layout == layout:
                routes = calculateMachineSequencesFromOperationSequence(process, layout)
                for route in routes:
                    route.insert(0, machine)
                    result.append(route)
        process.insert(0, processStep)
        return result
    else:
        return [[]]

def calculateMachineSequences(objectType: ProductType, layout: Layout):
    result: list[list[Machine]] = []
    processes = calculateOperationSequences(objectType)
    for process in processes:
        processRoutes = calculateMachineSequencesFromOperationSequence(process, layout)
        for processRoute in processRoutes:
            result.append(processRoute)
    return result


def calculateOperationSequences(objectType: ProductType):
    result: list[list[OperationType]] = []
    for operationType in objectType.producing_operations:
        prefixes = calculateOperationSequences(operationType.consumes_product_type)
        if not prefixes:
            result.append([operationType])
        else:
            for prefix in prefixes:
                prefix.append(operationType)
                result.append(prefix)
    return result
