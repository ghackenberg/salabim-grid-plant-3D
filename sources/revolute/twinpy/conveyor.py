import salabim as sim

from .vector import Vector

class Conveyor(sim.Component):
    def setup(self, source_position: Vector, target_position: Vector):
        # Positions
        self.source_position = source_position
        self.target_position = target_position

        # Distance
        self.distance = 0
        self.distance_time = self.env.now()

        # Stores
        self.store_in = sim.Store(name = "in", capacity = 1)
        self.store_out = sim.Store(name = "out", capacity = 1)

        # Line
        self.line = sim.AnimateLine(
            spec = [source_position.x, source_position.y, target_position.x, target_position.y],
            linecolor = "black",
            linewidth = 2
        )

    def process(self):
        pass