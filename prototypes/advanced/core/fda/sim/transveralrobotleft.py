import salabim as sim

from ..model import *
from .traversalrobot import *
from .job import *

class TransversalRobotLeft(TransversalRobot):
    def __init__(self, layout: Layout, corridor: Corridor, scenario: Scenario, env: sim.Environment, corridor_stores: list[sim.Store], machine_stores: list[list[sim.Store]], x: float, y: float, z: float):
        super().__init__(layout, corridor, scenario, env, corridor_stores, machine_stores, x, y, z)

    def process(self):
        duration = 1

        while True:
            # Pick from storage
            job: Job = yield self.from_store(self.corridor_store_left)
            # Move down
            yield from self.move_z(1.25, duration)
            # Move up
            yield from self.move_z(2.5, duration)

            # While next machine is in the same corridor and side
            while len(job.machine_sequence) > 0 and job.machine_sequence[0].corridor == self.corridor and job.machine_sequence[0].left:
                # Get machine
                machine = job.machine_sequence[0]
                # Calculate machine index
                machine_num = self.corridor.machinesLeft.index(machine)
                # Get stores
                machine_stores = self.machine_stores[machine_num]
                # Calculate machine position
                x = 3 + machine_num * 2
                # Check if we are at the machine
                if self.x != x:
                    # Move to machine
                    yield from self.move_x(x, duration)
                # Move down
                yield from self.move_z(1.5, duration)
                # Hand over
                yield self.to_store(machine_stores[0], job)
                # Move up
                yield from self.move_z(2.5, duration)
                # Wait for hand over
                job: Job = yield self.from_store(machine_stores[1])
                # Move down
                yield from self.move_z(1.5, duration)
                # Move up
                yield from self.move_z(2.5, duration)

            # Check if we are not at inventory
            if self.x != 1:
                # Move back to inventory
                yield from self.move_x(1, duration)
            # Move down
            yield from self.move_z(1.25, duration)
            # Place to storage
            yield self.to_store(self.corridor_store_main, job)
            # Move up
            yield from self.move_z(2.5, duration)