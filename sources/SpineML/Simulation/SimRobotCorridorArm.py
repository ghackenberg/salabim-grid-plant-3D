import salabim as sim

from ..Configuration import Corridor, Machine

from .SimRobot import SimRobot
from .SimMachine import SimMachine
from .SimOrderJob import SimOrderJob

class SimRobotCorridorArm(SimRobot):
    def __init__(self, corridor: Corridor, machines: list[Machine], direction: str, store_in: sim.Store, store_out_arm: sim.Store, store_out_main: sim.Store, sim_machines: list[SimMachine], dx: float, y: float, *args, **kwargs):
        super().__init__(f"Arm {direction} robot", 2, dx, y, 2.5, "green", *args, **kwargs)

        self.corridor = corridor
        self.machines = machines

        self.direction = direction

        self.store_in = store_in
        self.store_out_arm = store_out_arm
        self.store_out_main = store_out_main

        self.dx = dx

        self.sim_machines = sim_machines

    def process(self):
        # Debug output
        print(f"[t={self.env.now()}] Starting {self.corridor.name} arm {self.direction} robot")

        speed = 1
        while True:
            # Debug output
            print(f"[t={self.env.now()}] {self.corridor.name} arm {self.direction} robot waiting for job")
            # Pick from storage
            job: SimOrderJob = yield self.from_store(self.store_in)
            # Move down
            yield from self.move_z(1.25, speed)
            # Update state
            self.state_load.set("loaded")
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
                # Debug output
                print(f"[t={self.env.now()}] {self.corridor.name} arm {self.direction} robot moving to {sim_machine.machine.name}")
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
                # Update state
                self.state_load.set("empty")
                # Move up
                yield from self.move_z(2.5, speed)
                # Debug output
                print(f"[t={self.env.now()}] {self.corridor.name} arm {self.direction} robot waiting for job")
                # Wait for hand over
                job: SimOrderJob = yield self.from_store(sim_machine.store_out)
                # Move down
                yield from self.move_z(1.5, speed)
                # Upadte state
                self.state_load.set("loaded")
                # Update machine state
                sim_machine.state.set("waiting")
                # Move up
                yield from self.move_z(2.5, speed)
            # Debug output
            print(f"[t={self.env.now()}] {self.corridor.name} arm {self.direction} robot moving to corridor storage")
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
            # Update state
            self.state_load.set("empty")
            # Move up
            yield from self.move_z(2.5, speed)

        # Debug output
        print(f"[t={self.env.now()}] {self.corridor.name} arm {self.direction} robot finished")
