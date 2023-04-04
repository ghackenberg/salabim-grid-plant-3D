import salabim as sim

class Robot(sim.Component):
    def __init__(self, env: sim.Environment, x: float, y: float, z: float, color: str):
        super().__init__()

        self.env = env

        self.x = x
        self.y = y
        self.z = z
        self.t = env.now()

        self.next_x = x
        self.next_y = y
        self.next_z = z
        self.next_t = env.now()

        sim.Animate3dBox(x_len=0.5, y_len=0.5, z_len=0.5, color=color, edge_color='white', x=self.x_func, y=self.y_func, z=self.z_func)

    def x_func(self, t: float):
        if self.next_t == self.t:
            return self.x
        else:
            return self.x + (self.next_x - self.x) * (t - self.t) / (self.next_t - self.t)
    
    def y_func(self, t: float):
        if self.next_t == self.t:
            return self.y
        else:
            return self.y + (self.next_y - self.y) * (t - self.t) / (self.next_t - self.t)

    def z_func(self, t: float):
        if self.next_t == self.t:
            return self.z
        else:
            return self.z + (self.next_z - self.z) * (t - self.t) / (self.next_t - self.t)
        
    def move_x(self, next_x: float, duration: float):
        self.next_x = next_x
        self.next_t = self.env.now() + duration
        yield self.hold(duration)
        self.x = self.next_x
        
    def move_y(self, next_y: float, duration: float):
        self.next_y = next_y
        self.next_t = self.env.now() + duration
        yield self.hold(duration)
        self.y = self.next_y
        
    def move_z(self, next_z: float, duration: float):
        self.next_z = next_z
        self.next_t = self.env.now() + duration
        yield self.hold(duration)
        self.z = self.next_z