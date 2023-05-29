import salabim as sim

from .model import *
from .sim import *


def simulate(layout: Layout, scenario: Scenario, animate=False):
    # Create environment
    env = sim.Environment(time_unit='hours')

    # Enable animation (if requested)
    if animate:
        # Setup 2D window
        env.width(950)
        env.height(768)
        env.position((960, 100))
        # Setup 3D window
        env.width3d(950)
        env.height3d(768)
        env.position3d((0, 100))
        # Setup 2D/3D overlays
        env.show_camera_position(True)
        env.show_camera_position(over3d=True)
        # Setup 3D camera
        env.view(x_eye=0, y_eye=15, z_eye=5)
        # Enable 2D/3D animation
        env.animation_parameters(animate=True, animate3d=True, show_fps=True)

    # Create components
    sim_layout = SimLayout(layout, scenario, env)
    sim_scenario = SimScenario(layout, scenario, env, sim_layout.store_start)

    # Perform simulation
    env.run()

    # Print statistics
    sim_scenario.printStatistics()
    sim_layout.printStatistics()
