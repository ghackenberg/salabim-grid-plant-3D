import salabim as sim

from .vector import Vector
from .robot import Robot
from .machine import Machine
from .conveyor import Conveyor

class Product(sim.Component):
    def setup(self, position):
        # Position
        self.position = position

        # State
        self.state = sim.State("state")

        # Rectangle
        self.rectangle = sim.AnimateRectangle(
            spec = lambda t: self.calculate_rectangle_spec(t),
            text = "P",
            fillcolor = "red",
            textcolor = "white"
        )
    
    def calculate_rectangle_spec(self, time: float):
        if isinstance(self.position, Robot):
            x = self.position.calculate_joint_circle_x(3, time)
            y = self.position.calculate_joint_circle_y(3, time)
        elif isinstance(self.position, Machine):
            [x, y] = self.position.position
        elif isinstance(self.position, Conveyor):
            [x, y] = self.position.source_position
        elif isinstance(self.position, Vector):
            x = self.position.x
            y = self.position.y
        return [x - 10, y - 10, x + 10, y + 10]

    def process(self):
        pass