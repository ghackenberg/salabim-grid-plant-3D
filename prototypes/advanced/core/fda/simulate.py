import salabim as sim

from .model import *

def simulate(layout: Layout, scenario: Scenario):
    #General visualization commands
    env = sim.Environment()

    env.width3d(900)
    env.height3d(700)
    env.position3d((0, 100))

    env.animate(True)
    env.animate3d(True)

    env.show_camera_position(over3d=True)

    env.view(x_eye=5, y_eye=15, z_eye=7.5)

    sim.Animate3dGrid(x_range=range(-2, 10), y_range=range(-2, 10))

    #Transversal corridors counting
    corridor_count = len(layout.corridors)

    # Draw backbone (main corridor)
    sim.Animate3dBox(x_len=0.5, y_len=corridor_count * 2 + 1.5, z_len=0.5, color="red", x=0, y=0, z=2.5)
    # Down (connection robot-machine)
    sim.Animate3dBox(x_len=0.5, y_len=0.5, z_len=1.25, color="red", x=0, y=+2 + (corridor_count / 2), z=1.625)
    sim.Animate3dBox(x_len=0.5, y_len=0.5, z_len=1.25, color="red", x=0, y=-2 - (corridor_count / 2), z=1.625)
    # Robot
    sim.Animate3dBox(x_len=1, y_len=1, z_len=1, color="red", x=0, y=0, z=2.5)

    # Storage Areas in the main corridor
    sim.Animate3dBox(x_len=3, y_len=1, z_len=1, color="orange", x=0, y=+2 + (corridor_count / 2), z=0.5)
    sim.Animate3dBox(x_len=3, y_len=1, z_len=1, color="orange", x=0, y=-2 - (corridor_count / 2), z=0.5)

    # Draw corridor (Transversal corridors)
    corridor_num = 0
    for corridor in layout.corridors:
        machine_left_count = len(corridor.machinesLeft)
        machine_right_count = len(corridor.machinesRight)

        y = (corridor_num + 0.5 - corridor_count/2)*2

        # Robot
        sim.Animate3dBox(x_len=1, y_len=1, z_len=1, color="green", x=-1, y=y, z=2.5)
        sim.Animate3dBox(x_len=1, y_len=1, z_len=1, color="green", x=1, y=y, z=2.5)
        # Down
        sim.Animate3dBox(x_len=0.5, y_len=0.5, z_len=1.25, color="green", x=-1, y=y, z=1.625)
        sim.Animate3dBox(x_len=0.5, y_len=0.5, z_len=1.25, color="red", x=0, y=y, z=1.625)
        sim.Animate3dBox(x_len=0.5, y_len=0.5, z_len=1.25, color="green", x=1, y=y, z=1.625)

        # Storage Area
        sim.Animate3dBox(x_len=3, y_len=1, z_len=1, color="orange", x=0, y=y, z=0.5)

        x_len_left = machine_left_count * 2 + 0.5
        x_len_right = machine_right_count * 2 + 0.5

        x_left = - 0.75 - x_len_left / 2
        x_right = + 0.75 + x_len_right / 2

        sim.Animate3dBox(x_len=x_len_left, y_len=0.5, z_len=0.5, color="green", x=x_left, y=y, z=2.5)
        sim.Animate3dBox(x_len=x_len_right, y_len=0.5, z_len=0.5, color="green", x=x_right, y=y, z=2.5)

        # Draw machine isntances
        machine_num = 0
        for machine in corridor.machinesLeft:
            x = -3 - machine_num * 2
            # Down
            sim.Animate3dBox(x_len=0.5, y_len=0.5, z_len=1.25, color="green", x=x, y=y, z=1.625)
            # Machine
            sim.Animate3dBox(x_len=1, y_len=1, z_len=1, color="blue", x=x, y=y, z=0.5)
            machine_num = machine_num + 1

        machine_num = 0
        for machine in corridor.machinesRight:
            x = +3 + machine_num * 2
            # Down
            sim.Animate3dBox(x_len=0.5, y_len=0.5, z_len=1.25, color="green", x=x, y=y, z=1.625)
            # Machine
            sim.Animate3dBox(x_len=1, y_len=1, z_len=1, color="blue", x=x, y=y, z=0.5)
            machine_num = machine_num + 1

        corridor_num = corridor_num + 1

    env.run(sim.inf)
