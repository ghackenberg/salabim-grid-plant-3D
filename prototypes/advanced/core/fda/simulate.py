import salabim as sim

from .model import *
from .sim import *
from .sim import statistics


def simulate(layout: Layout, scenario: Scenario):
    #Visualization settings
    env = sim.Environment(time_unit='hours')

    env.width(950)
    env.height(768)
    env.position((960, 100))

    env.width3d(950)
    env.height3d(768)
    env.position3d((0, 100))

    env.animate(True)
    env.animate3d(True)

    env.show_camera_position(True)
    env.show_camera_position(over3d=True)

    env.view(x_eye=0, y_eye=15, z_eye=5)

    sim.Animate3dGrid(x_range=range(-20, 20), y_range=range(-20, 20))

    # Tool
    Tool(PROCESS_STEPS)

    # Create stores per corridor
    start_store = sim.Store("start")
    corridor_stores: list[list[sim.Store]] = []
    for corridor in layout.corridors:
        store_main = sim.Store(f"{corridor.code} main") #it is the part of the storage that is accessed by the main robot
        store_left = sim.Store(f"{corridor.code} left") #it is the part of the storage that is accessed by the robot of the left t_corridor
        store_right = sim.Store(f"{corridor.code} right")
        corridor_stores.append([store_main, store_left, store_right]) #append the possible corridors' parts in the list of corridords
    end_store = sim.Store("end")


    # Create jobs
    job = []
    for order in scenario.orders: #per each order creates a job
        for i in range(order.quantity):
            job_var = Job(layout, scenario, order, start_store)
            job.append(job_var)


    #Transversal corridors counting
    corridor_count = len(layout.corridors) #numbers of t_corridors in a certain layout
    y = 2 + corridor_count / 1.15

    # Draw backbone (main corridor)
    sim.Animate3dBox(x_len=0.25, y_len=y*2.07, z_len=0.25, color="red", x=0, y=0, z=2.5)

    # Down from main corridor to RM/FP storage areas
    sim.Animate3dBox(x_len=0.25, y_len=0.25, z_len=1.5, color="red", x=0, y=y, z=1.625)
    sim.Animate3dBox(x_len=0.25, y_len=0.25, z_len=1.5, color="red", x=0, y=-y, z=1.625)

    # Robot
    MainRobot(layout, scenario, env, start_store, corridor_stores, end_store, 0, 2.5)

    # Storage Areas in the main corridor
    sim.Animate3dBox(x_len=3, y_len=1, z_len=1, color="yellow", x=0, y=y, z=0.5)
    sim.Animate3dBox(x_len=3, y_len=1, z_len=1, color="yellow", x=0, y=-y, z=0.5)

    # Draw corridor (Transversal corridors)
    corridor_num = 0
    for corridor in layout.corridors: #for each corridor in the layout, define the number of machines in left and right corridor
        # Create left machine stores
        machine_stores_left: list[list[sim.Store]] = []
        for machine in corridor.machinesLeft:
            store_in = sim.Store(f"{machine.name} in")
            store_out = sim.Store(f"{machine.name} out")
            machine_stores_left.append([store_in, store_out])
        
        # Create right machine stores
        machine_stores_right: list[list[sim.Store]] = []
        for machine in corridor.machinesRight:
            store_in = sim.Store(f"{machine.name} in")
            store_out = sim.Store(f"{machine.name} out")
            machine_stores_right.append([store_in, store_out])

        machine_left_count = len(corridor.machinesLeft)
        machine_right_count = len(corridor.machinesRight)

        y = (corridor_num + 0.5 - corridor_count/2)*2

        # Robot
        #if there is no machine in the corridor then we don't need the robot
        if machine_left_count != 0:
            TransversalRobotLeft(layout, corridor, scenario, env, corridor_stores[corridor_num], machine_stores_left, +1, y, 2.5)
        else:
            False
        
        #if there is no machine in the corridor then we don't need the robot
        if machine_right_count != 0:
            TransversalRobotRight(layout, corridor, scenario, env, corridor_stores[corridor_num], machine_stores_right, -1, y, 2.5)
        else:
            False

        # Down (connection robot storage areas in t_corridors)
        sim.Animate3dBox(x_len=0.25, y_len=0.25, z_len=1.5, color="red", x=0, y=y, z=1.625)
        if machine_left_count != 0:
            sim.Animate3dBox(x_len=0.25, y_len=0.25, z_len=1.5, color="green", x=+1, y=y, z=1.625)
        else:
            False
        if machine_right_count != 0:
            sim.Animate3dBox(x_len=0.25, y_len=0.25, z_len=1.5, color="green", x=-1, y=y, z=1.625)
        else:
            False

        # Storage Area in t_corridors
        x_len = 3
        y_len = 1
        z_len = 1
        sim.Animate3dBox(x_len=x_len, y_len=y_len, z_len=z_len, color= 'orange', x=0, y=y, z=0.5)

        # Transversal corridors, left-right
        x_len_left = machine_left_count * 2 + 0.26
        x_len_right = machine_right_count * 2 + 0.26

        x_left = +0.86 + x_len_left / 2
        x_right = - 0.86 - x_len_right / 2
        if machine_left_count != 0:
            sim.Animate3dBox(x_len=x_len_left, y_len=0.25, z_len=0.25, color="green", x=x_left, y=y, z=2.5)
        else:
            False
        if machine_right_count != 0:
            sim.Animate3dBox(x_len=x_len_right, y_len=0.25, z_len=0.25, color="green", x=x_right, y=y, z=2.5)
        else:
            False

        # Draw machine instances
        machine_num = 0
        for machine in corridor.machinesLeft:
            x = +3 + machine_num * 2
            stores = machine_stores_left[machine_num]
            sim_machine = SimMachine(machine, env, stores[0], stores[1], x, y) #[0]=store_in, [1]=store_out
            print(statistics.utilisation_values(PROCESS_STEPS, MACHINES, layout, sim_machine.total_availability))

            # Print machine code over each machine
            #code = str(machine.machineType.code)
            #sim.AnimateText(code, x, y+4, font= 'Calibri', fontsize=45, textcolor='pink', text_anchor='c')

            machine_num = machine_num + 1

        machine_num = 0
        for machine in corridor.machinesRight:
            x = -3 - machine_num * 2
            stores = machine_stores_right[machine_num]
            sim_machine = SimMachine(machine, env, stores[0], stores[1], x, y)
            print(statistics.utilisation_values(PROCESS_STEPS, MACHINES, layout, sim_machine.total_availability))

            # Print machine code over each machine
            #code = str(machine.machineType.code)
            #sim.AnimateText(code, x, y+4, fontsize=15, textcolor='orange')

            machine_num = machine_num + 1

        corridor_num = corridor_num + 1




    env.run(sim.inf)