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
            print(f"[{self.env.now()}] Maschine wartet auf Produkt von Roboter")
            self.state.set("idle")
            product = self.from_store(self.store_in)
            if isinstance(product, Product):
                product.position = self
            # Work
            print(f"[{self.env.now()}] Maschine bearbeitet Produkt")
            self.state.set("work")
            self.hold(2)
            # Done
            print(f"[{self.env.now()}] Maschine übergibt Produkt an Roboter")
            self.to_store(self.store_out, product)