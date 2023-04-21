import salabim as sim

from ..simulate import*
from ..model import *
from .job import *
from .toollife import *

class ToolMov(sim.Component):
    def __init__(self, machine: Machine, process: PROCESS_STEPS, env: sim.Environment, x: float):
        super().__init__()

        # Remember machine
        self.machine = machine
        # Remember process
        self.process = process

        self.env = env

        self.x = x
        self.t = env.now()

        self.next_x = x
        self.next_t = env.now()

        m = 0
        for toolType in MACHINETYPE_TOOLTYPE_MAP[machine.machineType]:
            sim.Animate3dBox(x_len=0.05, y_len=0.05, z_len=0.18, color='blue',  x=self.x_func+m, y=y + 0.25, z=1.10)
            m = m - 0.1

    def x_func(self, t: float):
        if self.next_t == self.t:
            return self.x
        else:
            return self.x - (self.next_x - self.x) * (t - self.t) / (self.next_t - self.t)

    def move_x(self, next_x: float, speed: float):
        duration = abs(next_x - self.x) / speed
        self.t = self.env.now()
        self.next_x = next_x
        self.next_t = self.env.now() + duration
        yield self.hold(duration)
        self.x = self.next_x