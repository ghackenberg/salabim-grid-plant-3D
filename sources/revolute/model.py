import salabim as sim

from twinpy import *

class RobotOne(Robot):
    def process(self):
        # Define target positions
        joint_angles_a = [0, 0, 0]
        joint_angles_b = [0, 45, 90]
        joint_angles_c = [0, -45, -90]
        # Process loop
        while True:
            # Motion sequence
            self.move_to(joint_angles_b, 2)
            self.move_to(joint_angles_c, 4)
            self.move_to(joint_angles_a, 2)
            # Pick
            print(f"[{self.env.now()}] Roboter holt Produkt")
            self.state.set("pick")
            self.hold(1)
            # Place
            print(f"[{self.env.now()}] Roboter übergibt Produkt an Maschine")
            self.state.set("place")
            self.to_store(machine1.store_in, Product(position = self))
            # Idle
            print(f"[{self.env.now()}] Roboter wartet auf Produkt von Maschine")
            self.state.set("idle")
            self.from_store(machine1.store_out)
            # Pick
            print(f"[{self.env.now()}] Roboter nimmt Produkt von Maschine")
            self.state.set("pick")
            self.hold(1)
            # Place
            print(f"[{self.env.now()}] Roboter gibt Produkt")
            self.state.set("place")
            self.hold(1)

class RobotTwo(Robot):
    def process(self):
        # Define target positions
        joint_angles_a = [0, 0, 0]
        joint_angles_b = [0, 45, 90]
        joint_angles_c = [0, -45, -90]
        # Process loop
        while True:
            # Motion sequence
            self.move_to(joint_angles_b, 2)
            self.move_to(joint_angles_c, 4)
            self.move_to(joint_angles_a, 2)

# Create simulation environment
env = sim.Environment()
env.modelname("Robotereinsatzplanung")

# Setup 2D or 3D animation
if True:
    # Animation (2D)
    env.animate(True)
    # Window
    env.width(800)
    env.height(600)
    env.position((100, 100))
    # Objects
    sim.AnimateRectangle(
        spec = (0, 0, 800, 100),
        text = "Floor",
        fillcolor = "lightgray",
        textcolor = "black",
        fontsize = 20
    )
    sim.AnimateRectangle(
        spec = (0, 500, 800, 600),
        text = "Ceiling",
        fillcolor = "lightgray",
        textcolor = "black",
        fontsize = 20
    )
else:
    # Animation (3D)
    env.animate3d(True)
    # Window
    env.width3d(800)
    nv.height3d(600)
    env.position3d((100, 100))
    # Objects
    sim.Animate3dGrid(x_range=range(-2, 2, 1), y_range=range(-2, 2, 1))

# Define conveyors
conveyor1 = Conveyor(source_position = Vector(100, 300), target_position = Vector(350, 300))
conveyor2 = Conveyor(source_position = Vector(450, 300), target_position = Vector(700, 300))
# Define machines
machine1 = Machine(position = Vector( 50, 300))
machine2 = Machine(position = Vector(400, 300))
machine3 = Machine(position = Vector(750, 300))
# Define robots
robot1 = RobotOne(base_position = Vector(200, 100), base_angle = 0)
robot2 = RobotTwo(base_position = Vector(400, 100), base_angle = 0)
robot3 = RobotTwo(base_position = Vector(600, 100), base_angle = 0)
robot4 = RobotTwo(base_position = Vector(200, 500), base_angle = 180)
robot5 = RobotTwo(base_position = Vector(400, 500), base_angle = 180)
robot6 = RobotTwo(base_position = Vector(600, 500), base_angle = 180)

# Start simulation with/without video production
if True:
    # Video production disabled
    env.run(sim.inf)
else:
    # Video production enabled
    env.video("test.mp4")
    env.run(till = 30)
    env.video_close()