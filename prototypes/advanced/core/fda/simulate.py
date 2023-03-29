import salabim as sim

from .model import *
from .sim import *


def simulate(layout: Layout, scenario: Scenario):
    #General visualization commands
    env = sim.Environment()

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

    sim.Animate3dGrid(x_range=range(-10, 10), y_range=range(-10, 10))

    #Transversal corridors counting
    corridor_count = len(layout.corridors) # numbers of t_corridors in a certain layout
    y = 2 + corridor_count / 1.5

    # Draw backbone (main corridor)
    sim.Animate3dBox(x_len=0.25, y_len=y*2.06, z_len=0.25, color="red", x=0, y=0, z=2.5)

    # Down (connection to the two storage areas)
    sim.Animate3dBox(x_len=0.25, y_len=0.25, z_len=1.5, color="red", x=0, y=y, z=1.625)
    sim.Animate3dBox(x_len=0.25, y_len=0.25, z_len=1.5, color="red", x=0, y=-y, z=1.625)

    # Robot
    MainRobot(layout, env, 0, 2.5)

    # Storage Areas in the main corridor
    sim.Animate3dBox(x_len=3, y_len=1, z_len=1, color="yellow", x=0, y=y, z=0.5)
    sim.Animate3dBox(x_len=3, y_len=1, z_len=1, color="yellow", x=0, y=-y, z=0.5)

    # Draw corridor (Transversal corridors)
    corridor_num = 0
    for corridor in layout.corridors: #for each corridor in the layout, define the number of machines in left and right corridor
        machine_left_count = len(corridor.machinesLeft)
        machine_right_count = len(corridor.machinesRight)

        y = (corridor_num + 0.5 - corridor_count/2)*2

        # Robot

        #if there is no machine in the corridor then we don't need the robot
        if machine_left_count != 0:
            TransversalRobotLeft(corridor, env, +1, y, 2.5)
        else:
            False
        
        #if there is no machine in the corridor then we don't need the robot
        if machine_right_count != 0:
            TransversalRobotRight(corridor, env, -1, y, 2.5)
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
            # Down
            sim.Animate3dBox(x_len=0.25, y_len=0.25, z_len=1.20, color="green", x=x, y=y, z=1.8)
            # Tool
            sim.Animate3dBox(x_len=0.05, y_len=0.05, z_len=0.18, color="blue", x=x, y=y+0.25, z=1.1)
            sim.Animate3dBox(x_len=0.05, y_len=0.18, z_len=0.05, color="white", x=x, y=y + 0.19, z=1.18)
            # Machine
            sim.Animate3dBox(x_len=0.60, y_len=0.40, z_len=0.40, color="white", x=x, y=y-0.08 , z=1)
            sim.Animate3dBox(x_len=0.60, y_len=0.70, z_len=0.60, color="white", x=x, y=y+0.08, z=0.5)
            machine_num = machine_num + 1

        machine_num = 0
        for machine in corridor.machinesRight:
            x = -3 - machine_num * 2
            # Down
            sim.Animate3dBox(x_len=0.25, y_len=0.25, z_len=1.20, color="green", x=x, y=y, z=1.8)
            # Tool
            sim.Animate3dBox(x_len=0.05, y_len=0.05, z_len=0.18, color="blue", x=x, y=y + 0.25, z=1.1)
            sim.Animate3dBox(x_len=0.05, y_len=0.18, z_len=0.05, color="white", x=x, y=y + 0.19, z=1.18)
            # Machine
            sim.Animate3dBox(x_len=0.60, y_len=0.40, z_len=0.40, color="white", x=x, y=y -0.08, z=1)
            sim.Animate3dBox(x_len=0.60, y_len=0.70, z_len=0.60, color="white", x=x, y=y+0.08, z=0.5)
            machine_num = machine_num + 1

        corridor_num = corridor_num + 1


    env.run(sim.inf)
