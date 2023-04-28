from .model import *

def calculateMachineSequencesFromProcessStepSequence(process: list[ProcessStep], layout: Layout):
    if len(process) > 0:
        result: list[list[Machine]] = []
        processStep = process.pop(0)
        for machine in processStep.machineType.machines:
            if machine.corridor.layout == layout:
                routes = calculateMachineSequencesFromProcessStepSequence(process, layout)
                for route in routes:
                    route.insert(0, machine)
                    result.append(route)
        process.insert(0, processStep)
        return result
    else:
        return [[]]

def calculateMachineSequences(objectType: ProductType, layout: Layout):
    result: list[list[Machine]] = []
    processes = calculateProcessStepSequences(objectType)
    for process in processes:
        processRoutes = calculateMachineSequencesFromProcessStepSequence(process, layout)
        for processRoute in processRoutes:
            result.append(processRoute)
    return result

def calculateProcessStepSequences(objectType: ProductType):
    result: list[list[ProcessStep]] = []
    for operationType in objectType.producingProcessSteps:
        prefixes = calculateProcessStepSequences(operationType.consumesProductType)
        if not prefixes:
            result.append([operationType])
        else:
            for prefix in prefixes:
                prefix.append(operationType)
                result.append(prefix)
    return result

