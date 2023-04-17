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


'''
def Tool(process: PROCESS_STEPS, layout: Layout, x: float, y: float):
    sim.Animate3dBox(x_len=0.05, y_len=0.18, z_len=0.05, color="white", x=x, y=y + 0.19, z=1.18)
    if len(process) > 0:
        for i in range(len(process)): #per ogni processo voglio sapere che macchina e che tool lo eseguono
            for j in range(i+1, len(process)):
                #m = 0.25
                #n = 0.19
                if process[i] != process[j] and process[i].machineType == process[j].machineType and process[i].toolType != process[j].toolType:
                    #sim.Animate3dBox(x_len=0.05, y_len=0.05, z_len=0.18, color="blue",  x=x, y=y+m, z=1.10)
                    #m=m*2
                    #n=n*2
                    print (i)
                    print (j)
                    print("La macchina {} ha {}, {}".format(process[i].machineType, process[i].toolType, process[j].toolType))

                else:
                    #sim.Animate3dBox(x_len=0.05, y_len=0.05, z_len=0.18, color="blue", x=x, y=y + 0.25, z=1.10)
                #se non si rientra in questa casistca:
                    #disegna solo un tool



       
        for machine in processStep.machineType.machines:
            if machine.corridor.layout == layout: #if the machine is the layout that we are considering
                '''
