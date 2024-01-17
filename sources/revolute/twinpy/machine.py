import salabim as sim

class Machine(sim.Component):

    from .vector import Vector

    def setup(self, position: Vector):
        self.position = position
        # Define state
        self.state = sim.State(name = "state", value = "idle")
        # Define stores
        self.store_in = sim.Store(name = "in", capacity = 1)
        self.store_out = sim.Store(name = "out", capacity = 1)

    def process(self):
        from .product import Product
        # Process loop
        while True:
            # Idle
            self.state.set("idle")
            # Take
            product = self.from_store(self.store_in)
            # Attach
            if isinstance(product, Product):
                product.position_controller = self
            # Work
            self.state.set("work")
            self.hold(2)
            # Give
            self.to_store(self.store_out, product)