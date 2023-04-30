from ..model import *

def Tool(process: PROCESS_STEPS):
    for i in range(len(process)):
        machineType = process[i].machineType
        if(machineType not in MACHINETYPE_TOOLTYPE_MAP):
            toolTypeArray = [process[i].toolType]
            MACHINETYPE_TOOLTYPE_MAP[machineType] = toolTypeArray
        else:
            toolTypeArray = MACHINETYPE_TOOLTYPE_MAP[machineType]
            toolTypeArray.append(process[i].toolType)
            MACHINETYPE_TOOLTYPE_MAP.update({machineType : toolTypeArray})
    return (MACHINETYPE_TOOLTYPE_MAP)


MACHINETYPE_TOOLTYPE_MAP = {}