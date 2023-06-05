import salabim as sim

from .corridor import *
from .layout import *
from .robot import *
from ..model import *


class SimMainRobot(SimRobot):
    def __init__(self, layout: Layout, scenario: Scenario, env: sim.Environment, store_start: sim.Store, store_end: sim.Store, sim_corridors: list[SimCorridor], y: float, z: float):
        super().__init__("Main robot", 0, env, 0, y, z, "red")

        self.layout = layout
        self.scenario = scenario

        self.store_start = store_start
        self.store_end = store_end

        self.sim_corridors = sim_corridors

    def process(self) :
        # duration of movement between stores
        speed = 1
        # numbers of t_corridors in a certain layout
        corridor_count = len(self.layout.corridors)
        # position of the start and the end store
        y_stock = 2 + corridor_count / 1.15

        while True:
            # Move to RM inventory
            yield from self.move_y(-y_stock, speed)
            # Move down
            yield from self.move_z(1.25, speed)
            # Pick next job
            job: SimJob = yield self.from_store(self.store_start)
            # Update state
            self.state_load.set("loaded")
            # Move up
            yield from self.move_z(2.5, speed)
            # Check if machines are missing
            while len(job.machine_sequence) > 0:
                # Get next machine
                machine = job.machine_sequence[0]
                # Find corridor number
                corridor_num = self.layout.corridors.index(machine.corridor)
                # Get sim corridor
                sim_corridor = self.sim_corridors[corridor_num]
                # Compute corridor position
                y = (corridor_num + 0.5 - corridor_count / 2) * 2
                # Check if we need to move to the corridor
                if y != self.y:
                    # Move to the corridor
                    yield from self.move_y(y, speed)
                # Move down
                yield from self.move_z(1.25, speed)
                # Pass to left or right store
                if machine.left:
                    # Pass to left store
                    yield self.to_store(sim_corridor.store_left, job)
                else:
                    # Pass to right store
                    yield self.to_store(sim_corridor.store_right, job)
                # Update state
                self.state_load.set("empty")
                # Move up
                yield from self.move_z(2.5, speed)
                # Take from corridor store
                job: SimJob = yield self.from_store(sim_corridor.store_main)
                # Move down
                yield from self.move_z(1.25, speed)
                # Update state
                self.state_load.set("loaded")
                # Move up
                yield from self.move_z(2.5, speed)
            # Move to FP inventory
            yield from self.move_y(y_stock, speed)
            # Move down
            yield from self.move_z(1.25, speed)
            # Pass to queue
            yield self.to_store(self.store_end, job)
            # Update state
            self.state_load.set("empty")
            # Move up
            yield from self.move_z(2.5, speed)
