import salabim as sim

class Product(sim.Component):
    def setup(self):
        # Position
        self.position = None

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
        return [40, 290, 60, 310]

    def process(self):
        pass