import salabim as sim

class Conveyor(sim.Component):
    def setup(self, spec: list[float]):
        # States
        self.speed = sim.State(name = "speed", value = 1)

        # Stores
        self.store_in = sim.Store(name = "in", capacity = 1)
        self.store_out = sim.Store(name = "out", capacity = 1)

        # Line
        self.line = sim.AnimateLine(
            spec = spec,
            linecolor = "black",
            linewidth = 2
        )

    def process(self):
        pass