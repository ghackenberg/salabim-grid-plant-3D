import salabim as sim

from ..model import *
from .robot import *
from .machine import *

class TransversalRobot(Robot):
    def __init__(self, corridor: Corridor, machines: list[Machine], env: sim.Environment, store_in: sim.Store, store_out_arm: sim.Store, store_out_main: sim.Store, sim_machines: list[SimMachine], x: float, y: float):
        super().__init__(env, x, y, 2.5, "green")

        self.corridor = corridor
        self.machines = machines

        self.store_in = store_in
        self.store_out_arm = store_out_arm
        self.store_out_main = store_out_main

        self.dx = x

        self.sim_machines = sim_machines

    def process(self):
        speed = 1
        while True:
            # Pick from storage
            job: SimJob = yield self.from_store(self.store_in)
            # Move down
            yield from self.move_z(1.25, speed)
            # Move up
            yield from self.move_z(2.5, speed)
            # While next machine is in the same corridor and side
            while len(job.machine_sequence) > 0 and job.machine_sequence[0] in self.machines:
                # Get machine
                machine = job.machine_sequence[0]
                # Calculate machine index
                machine_num = self.machines.index(machine)
                # Get stores
                sim_machine = self.sim_machines[machine_num]
                # Calculate machine position
                x = (3 + machine_num * 2) * self.dx
                # Check if we are at the machine
                if self.x != x:
                    # Move to machine
                    yield from self.move_x(x, speed)
                # Move down
                yield from self.move_z(1.5, speed)
                # Hand over
                yield self.to_store(sim_machine.store_in, job)
                # Move up
                yield from self.move_z(2.5, speed)
                # Wait for hand over
                job: SimJob = yield self.from_store(sim_machine.store_out)
                # Move down
                yield from self.move_z(1.5, speed)
                # Update machine state
                sim_machine.state.set("waiting")
                # Move up
                yield from self.move_z(2.5, speed)
            # Check if we are not at inventory
            if self.x != self.dx:
                # Move back to inventory
                yield from self.move_x(self.dx, speed)
            # Move down
            yield from self.move_z(1.25, speed)
            # To main corridor or to other arm
            if len(job.machine_sequence) > 0 and job.machine_sequence[0].corridor == self.corridor:
                # Place to storage
                yield self.to_store(self.store_out_arm, job)
            else:
                # Place to storage
                yield self.to_store(self.store_out_main, job)
            # Move up
            yield from self.move_z(2.5, speed)
