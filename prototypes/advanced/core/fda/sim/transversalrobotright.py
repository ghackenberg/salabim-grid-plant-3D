import salabim as sim

from ..model import *
from .traversalrobot import *
from .job import *

class TransversalRobotRight(TransversalRobot):
    def __init__(self, layout: Layout, corridor: Corridor, scenario: Scenario, env: sim.Environment, corridor_stores: list[sim.Store], machine_stores: list[list[sim.Store]], x: float, y: float, z: float):
        super().__init__(layout, corridor, scenario, env, corridor_stores, machine_stores, x, y, z)

    def process(self):
        speed = 1

        while True:
            # Pick from storage
            job: Job = yield self.from_store(self.corridor_store_right)
            # Move down
            yield from self.move_z(1.25, speed)
            # Move up
            yield from self.move_z(2.5, speed)

            # While next machine is in the same corridor and side
            while len(job.machine_sequence) > 0 and job.machine_sequence[0].corridor == self.corridor and not job.machine_sequence[0].left:
                #while there is a job to process for the machine in the right part of the corridord

                # Get machine
                machine = job.machine_sequence[0]
                # Calculate machine index
                machine_num = self.corridor.machinesRight.index(machine)
                # Get stores
                machine_stores = self.machine_stores[machine_num]
                # Calculate machine position
                x = -3 + machine_num * 2
                # Check if we are at the machine
                if self.x != x:
                    # Move to machine
                    yield from self.move_x(x, speed)
                # Move down
                yield from self.move_z(1.5, speed)
                # Hand over
                yield self.to_store(machine_stores[0], job)
                # Move up
                yield from self.move_z(2.5, speed)
                # Wait for hand over
                job: Job = yield self.from_store(machine_stores[1])
                # Move down
                yield from self.move_z(1.5, speed)
                # Move up
                yield from self.move_z(2.5, speed)

            # Check if we are not at inventory
            if self.x != -1:
                # Move back to inventory
                yield from self.move_x(-1, speed)
            # Move down
            yield from self.move_z(1.25, speed)
            # To main robot or to left robot?
            if len(job.machine_sequence) > 0 and job.machine_sequence[0].corridor == self.corridor:
                # Place to storage
                yield self.to_store(self.corridor_store_left, job)
            else:
                # Place to storage
                yield self.to_store(self.corridor_store_main, job)
            # Move up
            yield from self.move_z(2.5, speed)