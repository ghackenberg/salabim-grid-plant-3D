from .model import *

# Algorithms

def calculateProcessRoutes(process: list[ProcessStep], layout: Layout):
    if len(process) > 0:
        result: list[list[Machine]] = []
        processStep = process.pop(0)
        for machine in processStep.machineType.machines:
            if machine.corridor.layout == layout:
                routes = calculateProcessRoutes(process, layout)
                for route in routes:
                    route.insert(0, machine)
                    result.append(route)
        process.insert(0, processStep)
        return result
    else:
        return [[]]

def calculateRoutes(objectType: ProductType, layout: Layout):
    result: list[list[Machine]] = []
    processes = calculateProcesses(objectType)
    for process in processes:
        processRoutes = calculateProcessRoutes(process, layout)
        for processRoute in processRoutes:
            result.append(processRoute)
    return result

def calculateProcesses(objectType: ProductType):
    result: list[list[ProcessStep]] = []
    for operationType in objectType.producingProcessSteps:
        prefixes = calculateProcesses(operationType.consumesProductType)
        if not prefixes:
            result.append([operationType])
        else:
            for prefix in prefixes:
                prefix.append(operationType)
                result.append(prefix)
    return result

def calculateSources(objectType: ProductType):
    chains = calculateProcesses(objectType)
    result: list[ProductType] = []
    for chain in chains:
        if not chain[0].consumesProductType in result:
            result.append(chain[0].consumesProductType)
    return result