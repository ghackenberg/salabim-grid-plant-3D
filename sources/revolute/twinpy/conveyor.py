import salabim as sim

class Conveyor(sim.Component):

    from .vector import Vector

    def setup(self, source_position: Vector, target_position: Vector):
        
        from .product import Product

        # Positions
        self.source_position = source_position
        self.target_position = target_position

        # Distance
        self.distance = source_position.substract(target_position).length()

        # Speed
        self.speed = sim.State(name = "speed", value = 1)

        # Stores
        self.store_in = sim.Store(name = "in", capacity = 1)
        self.store_out = sim.Store(name = "out", capacity = 1)

        # Products
        self.products: list[Product] = []
        self.product_distances: list[float] = []
        self.product_distance_times: list[float] = []

        # Line
        self.line = sim.AnimateLine(
            spec = [source_position.x, source_position.y, target_position.x, target_position.y],
            linecolor = "black",
            linewidth = 2
        )

    
    def process(self):

        from .product import Product

        # Process loop
        while True:
            # Take
            product = self.from_store(self.store_in)
            # Attach
            if isinstance(product, Product):
                product.position_controller = self
                # Register
                self.products.append(product)
                self.product_distances.append(0)
                self.product_distance_times.append(self.env.now())