import salabim as sim

from .model import *



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
    #sim.Animate3dBox(x_len=0.5, y_len=0.5, z_len=0.5, color="red", edge_color= 'white', x=0, y=lambda t: t%2, z=lambda t: 2.5)


    class MainRobot(sim.Component):
        #movements
        def __init__(self, env: sim.Environment, y: float, z: float):
            super().__init__()

            self.env = env

            self.x = 0
            self.y = y
            self.z = z
            self.t = env.now()

            self.next_y = y
            self.next_z = z
            self.next_t = env.now()

            sim.Animate3dBox(x_len=0.5, y_len=0.5, z_len=0.5, color="red", edge_color='white', x=self.x, y=self.y_func,
                             z=self.z_func)

        def y_func(self, t: float):
            if self.next_t == self.t:
                return self.y
            else:
                return self.y + (self.next_y - self.y) * (t - self.t) / (self.next_t - self.t)

        def z_func(self, t: float):
            if self.next_t == self.t:
                return self.z
            else:
                return self.z + (self.next_z - self.z) * (t - self.t) / (self.next_t - self.t)


        def process(self) :
            duration = 1
            corridor_count = len(layout.corridors)  # numbers of t_corridors in a certain layout
            y_stock = 2 + corridor_count / 1.5

            corridor_num = 0

            for corridor in layout.corridors:  # for each corridor in the layout, define the number of machines in left and right corridor
                y = (corridor_num + 0.5 - corridor_count / 2) * 2

                #Go to the RM inventory
                self.next_y = -y_stock
                self.next_t = self.env.now() + duration
                yield self.hold(duration)
                self.y = self.next_y

                # Move down in the RM inventory
                self.next_z = 1.25
                self.next_t = self.env.now() + duration
                yield self.hold(duration)
                self.z = self.next_z

                # Move up
                self.next_z = 2.5
                self.next_t = self.env.now() + duration
                yield self.hold(duration)
                self.z = self.next_z

                # Move to one WIP inventory
                self.next_y = y #I'm defining the next position to reach
                self.next_t = self.env.now() + duration
                yield self.hold(duration)
                self.y = self.next_y #and I'm ansking to maintain it

                # Move down
                self.next_z = 1.25
                self.next_t = self.env.now() + duration
                yield self.hold(duration)
                self.z = self.next_z

                # Move up
                self.next_z = 2.5
                self.next_t = self.env.now() + duration
                yield self.hold(duration)
                self.z = self.next_z


                corridor_num = corridor_num + 1

            # Go to the FP inventory
            self.next_y = y_stock
            self.next_t = self.env.now() + duration
            yield self.hold(duration)
            self.y = self.next_y

            # Move down in the RM inventory
            self.next_z = 1.25
            self.next_t = self.env.now() + duration
            yield self.hold(duration)
            self.z = self.next_z

            # Move up
            self.next_z = 2.5
            self.next_t = self.env.now() + duration
            yield self.hold(duration)
            self.z = self.next_z


    #main robot position
    main_robot = MainRobot(env, 0, 2.5)


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

        class TransversalRobot_left(sim.Component):
            def __init__(self, env: sim.Environment, x: float, y: float, z: float):
                super().__init__()

                self.env = env

                self.x = x
                self.y = y
                self.z = z
                self.t = env.now()

                self.next_x = x
                self.next_z = z
                self.next_t = env.now()



                sim.Animate3dBox(x_len=0.5, y_len=0.5, z_len=0.5, color="green", edge_color='white', x=self.x_func,
                                 y=self.y, z=self.z_func)

            #movements
            def x_func(self, t: float):
                if self.next_t == self.t:
                    return self.x
                else:
                    return self.x + (self.next_x - self.x) * (t - self.t) / (self.next_t - self.t)

            def z_func(self, t: float):
                if self.next_t == self.t:
                    return self.z
                else:
                    return self.z + (self.next_z - self.z) * (t - self.t) / (self.next_t - self.t)

            def process(self):
                duration = 5

                x_len_left = machine_left_count * 2 + 0.38
                x_left = -0.86 - x_len_left / 2

                while True:
                    # Move Left

                    print("Move forward", self.env.now())
                    self.next_x = 1
                    self.next_t = self.env.now() + duration
                    yield self.hold(duration)
                    self.x = self.next_x

                    # Move down
                    print("Move down")
                    self.next_z = 1.2
                    self.next_t = self.env.now() + duration
                    yield self.hold(duration)
                    self.z = self.next_z

                    # Move up
                    print("Move up")
                    self.next_z = 2.5
                    self.next_t = self.env.now() + duration
                    yield self.hold(duration)
                    self.z = self.next_z

                    # Move Right
                    print("Move backward")
                    self.next_x = 0
                    self.next_t = self.env.now() + duration
                    yield self.hold(duration)
                    self.x = self.next_x

        class TransversalRobot_right(sim.Component):
            def __init__(self, env: sim.Environment, x: float, y: float, z: float):
                super().__init__()

                self.env = env

                self.x = x
                self.y = y
                self.z = z
                self.t = env.now()

                self.next_x = x
                self.next_z = z
                self.next_t = env.now()

                sim.Animate3dBox(x_len=0.5, y_len=0.5, z_len=0.5, color="green", edge_color='white', x=self.x_func,
                                 y=self.y, z=self.z_func)

            # movements
            def x_func(self, t: float):
                if self.next_t == self.t:
                    return self.x
                else:
                    return self.x + (self.next_x - self.x) * (t - self.t) / (self.next_t - self.t)

            def z_func(self, t: float):
                if self.next_t == self.t:
                    return self.z
                else:
                    return self.z + (self.next_z - self.z) * (t - self.t) / (self.next_t - self.t)

            def process(self):
                duration = 5

                x_len_right = machine_right_count * 2 + 0.38
                x_right = + 0.86 + x_len_right / 2

                while True:
                    # Move Left

                    print("Move forward", self.env.now())
                    self.next_x = 1  ######da risolvere
                    self.next_t = self.env.now() + duration
                    yield self.hold(duration)
                    self.x = self.next_x

                    # Move down
                    print("Move down")
                    self.next_z = 1.2
                    self.next_t = self.env.now() + duration
                    yield self.hold(duration)
                    self.z = self.next_z

                    # Move up
                    print("Move up")
                    self.next_z = 2.5
                    self.next_t = self.env.now() + duration
                    yield self.hold(duration)
                    self.z = self.next_z

                    # Move Right
                    print("Move backward")
                    self.next_x = 0
                    self.next_t = self.env.now() + duration
                    yield self.hold(duration)
                    self.x = self.next_x



        #if there is no machine in the corridor then we don't need the robot
        if machine_left_count != 0:
            transversal_robot = TransversalRobot_left(env, -1, y, 2.5)
        else:
            False
        if machine_right_count != 0:
            transversal_robot = TransversalRobot_right(env, +1, y, 2.5)
        else:
            False



        # Down (connection robot storage areas in t_corridors)
        sim.Animate3dBox(x_len=0.25, y_len=0.25, z_len=1.5, color="red", x=0, y=y, z=1.625)
        if machine_left_count != 0:
            sim.Animate3dBox(x_len=0.25, y_len=0.25, z_len=1.5, color="green", x=-1, y=y, z=1.625)
        else:
            False
        if machine_right_count != 0:
            sim.Animate3dBox(x_len=0.25, y_len=0.25, z_len=1.5, color="green", x=1, y=y, z=1.625)
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

        x_left = -0.86 - x_len_left / 2
        x_right = + 0.86 + x_len_right / 2
        if machine_left_count != 0:
            sim.Animate3dBox(x_len=x_len_left, y_len=0.25, z_len=0.25, color="green", x=x_left, y=y, z=2.5)
        else:
            False
        if machine_right_count != 0:
            sim.Animate3dBox(x_len=x_len_right, y_len=0.25, z_len=0.25, color="green", x=x_right, y=y, z=2.5)
        else:
            False

        #t_robot = TransversalRobot_left(env, x_left, y, 2.5)
        #t_robot = TransversalRobot_right(env, x_right, y, 2.5)


        # Draw machine instances
        machine_num = 0
        for machine in corridor.machinesLeft:
            x = -3 - machine_num * 2
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
            x = +3 + machine_num * 2
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
