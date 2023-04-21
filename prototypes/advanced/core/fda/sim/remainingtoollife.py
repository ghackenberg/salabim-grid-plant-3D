import salabim as sim

from ..model import *
from .machinetool import *
from .job import *


class RemainingToolLife(sim.Component):
    def __init__(self, env: sim.Environment,  x: float, y: float):
        super().__init__()
        print('ciao')
        self.env = env

        self.x = x
        self.y = y
        self.t = env.now()

        self.next_x = x
        self.next_t = env.now()

        z_bar = 0.70
        for toolType in MACHINETYPE_TOOLTYPE_MAP:
            #Remaining tool's life bar
            sim.Animate3dBox(x_len=self.x_func, y_len=0.5, z_len=0.6, color='green', edge_color='green', x=x, y=y + 0.4379, z=z_bar)
            z_bar = z_bar - 0.08

    def x_func(self, t: float):
        if self.next_t == self.t:
            return self.x
        else:
            return self.x - (self.next_x - self.x) * (t - self.t) / (self.next_t - self.t)



    def move_x(self, next_x: float, speed: float):
        decrement = abs(next_x - self.x) / speed
        self.t = self.env.now()
        self.next_x = next_x
        self.next_t = self.env.now() + decrement
        yield self.hold(decrement)
        self.x = self.next_x

