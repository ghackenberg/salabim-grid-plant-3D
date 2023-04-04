import salabim as sim

from ..model import *
from ..calculate import *
from .robot import *
from .job import *

class MainRobot(Robot):
    def __init__(self, layout: Layout, scenario: Scenario, env: sim.Environment, start_store: sim.Store, corridor_stores: list[list[sim.Store]], end_store: sim.Store, y: float, z: float):
        super().__init__(env, 0, y, z, "red")

        self.layout = layout
        self.scenario = scenario

        self.start_store = start_store
        self.corridor_stores = corridor_stores
        self.end_store = end_store

    def process(self) :
        # duration of movement between stores
        duration = 1
        # numbers of t_corridors in a certain layout
        corridor_count = len(self.layout.corridors)
        # position of the start and the end store
        y_stock = 2 + corridor_count / 1.5

        while True:
            # Move to RM inventory
            yield from self.move_y(-y_stock, duration)
            # Move down
            yield from self.move_z(1.25, duration)
            # Pick next job
            job: Job = yield self.from_store(self.start_store)
            # Move up
            yield from self.move_z(2.5, duration)
            # Loop through corridors
            while len(job.machine_sequence) > 0:
                # Get next machine
                machine = job.machine_sequence[0]
                # Find corridor number
                corridor_num = self.layout.corridors.index(machine.corridor)
                # Compute corridor position
                y = (corridor_num + 0.5 - corridor_count / 2) * 2
                # Is the corridor different than before?
                if y != self.y:
                    # Move to WIP inventory
                    yield from self.move_y(y, duration)
                # Move down
                yield from self.move_z(1.25, duration)
                # Pass to left or right store
                if machine.left:
                    # Pass to left store
                    yield self.to_store(self.corridor_stores[corridor_num][1], job)
                else:
                    # Pass to right store
                    yield self.to_store(self.corridor_stores[corridor_num][2], job)
                # Move up
                yield from self.move_z(2.5, duration)
                # Take from main store
                job: Job = yield self.from_store(self.corridor_stores[corridor_num][0])
                # Move down
                yield from self.move_z(1.25, duration)
                # Move up
                yield from self.move_z(2.5, duration)
            # Move to FP inventory
            yield from self.move_y(y_stock, duration)
            # Move down
            yield from self.move_z(1.25, duration)
            # Pass to queue
            yield self.to_store(self.end_store, job)
            # Move up
            yield from self.move_z(2.5, duration)