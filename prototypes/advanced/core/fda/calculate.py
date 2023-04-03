from .model import *

# Algorithms

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