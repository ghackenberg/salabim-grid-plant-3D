import salabim as sim
import matplotlib.pyplot as plt

from ..model import Machine, ToolType

from .job import SimJob


class SimMachine(sim.Component):
    def __init__(self, machine: Machine, env: sim.Environment, x: float, y: float):
        super().__init__()

        self.machine = machine

        self.env = env

        # Track state
        self.state = sim.State("State", value='waiting')

        # Remember currently mounted tool
        self.tool_type: ToolType = None

        # Compute all possible tool types
        self.tool_types = machine.machine_type.computeToolTypes()

        # Remember remaining life units per tool
        self.remaining_life_units: dict[ToolType, int] = {}
        self.remaining_life_units_t: dict[ToolType, float] = {}
        self.remaining_life_units_next: dict[ToolType, int] = {}
        self.remaining_life_units_next_t: dict[ToolType, float] = {}
        # Iterate over all possible process steps for the given machine type
        for tool_type in self.tool_types:
            # Initialize the remaining life units for the respective tool type
            self.remaining_life_units[tool_type] = tool_type.total_life_units
            self.remaining_life_units_t[tool_type] = env.now()
            self.remaining_life_units_next[tool_type] = tool_type.total_life_units
            self.remaining_life_units_next_t[tool_type] = env.now()

        # Job stores
        self.store_in = sim.Store(f"{machine.name} in")
        self.store_out = sim.Store(f"{machine.name} out")

        # Vertical box
        sim.Animate3dBox(x_len=0.25, y_len=0.25, z_len=1.20, color="green", x=x, y=y + 0.00, z=1.80)

        # Tool support
        sim.Animate3dBox(x_len=0.05, y_len=0.18, z_len=0.05, color="white", x=x, y=y + 0.19, z=1.18)
        sim.Animate3dBox(x_len=0.60, y_len=0.18, z_len=0.05, color="white", x=x, y=y + 0.19, z=1.18)
        
        # Toolbars
        m = 0
        for tool_type in self.tool_types:
            sim.Animate3dBox(x_len=0.05, y_len=0.05, z_len=0.18, color="blue", x=x + m, y=y + 0.25, z=1.10)
            m = m + 0.1

        # Life bars
        z = 0.70
        for tool_type in self.tool_types:
            x_len = (lambda tt: lambda t: self.x_func(tt, t))(tool_type)
            color = (lambda tt: lambda t: self.c_func(tt))(tool_type)
            sim.Animate3dBox(x_len=x_len, y_len=0.01, z_len=0.07, color=color, x=x, y=y + 0.4379, z=z)
            z = z - 0.08
        
        # Machine
        sim.Animate3dBox(x_len=0.60, y_len=0.40, z_len=0.40, color="white", x=x, y=y - 0.08, z=1.00)
        sim.Animate3dBox(x_len=0.60, y_len=0.70, z_len=0.60, color="white", x=x, y=y + 0.08, z=0.50)

    def x_func(self, tool_type: ToolType, t: float):
        rtlu = self.remaining_life_units[tool_type]
        rtlu_t = self.remaining_life_units_t[tool_type]
        rtlu_next = self.remaining_life_units_next[tool_type]
        rtlu_next_t = self.remaining_life_units_next_t[tool_type]
        if rtlu_next_t == rtlu_t:
            return rtlu / tool_type.total_life_units * 0.4
        else:
            return (rtlu + (rtlu_next - rtlu) * (t - rtlu_t) / (rtlu_next_t - rtlu_t)) / tool_type.total_life_units * 0.4

    def c_func(self, tool_type: ToolType):
        rtlu_t = self.remaining_life_units_t[tool_type]
        rtlu_next_t = self.remaining_life_units_next_t[tool_type]
        if tool_type == self.tool_type:
            if rtlu_t == rtlu_next_t:
                if self.state.get() == "unmounting":
                    return "orange"
                elif self.state.get() == "mounting":
                    return "yellow"
                else:
                    return "green"
            else:
                return "red"
        else:
            return "gray"

    def process(self):
        while True:
            # Take next job from store
            job: SimJob = yield self.from_store(self.store_in)
            # Retrieve next process step to perform
            operation = job.operation_sequence.pop(0)
            duration = operation.duration
            tool_type = operation.tool_type
            total_life_units = tool_type.total_life_units
            consumed_life_units = operation.consumes_life_units
            remaining_life_units = self.remaining_life_units[tool_type]
            # Remove own machine from machine sequence
            machine = job.machine_sequence.pop(0)
            # Assert that we are the machine to perform the step
            assert machine == self.machine
            # Check if tool is mounted
            if tool_type != self.tool_type:
                # Check if tool is mounted
                if self.tool_type is not None:
                    # Unmount tool
                    self.state.set("unmouting")
                    yield self.hold(self.tool_type.unmount_time)
                # Mount tool
                self.state.set("mounting")
                self.tool_type = tool_type
                yield self.hold(self.tool_type.mount_time)
                # Check if previous tool is too old
                if remaining_life_units < consumed_life_units:
                    # Update remaining life units
                    remaining_life_units = total_life_units
            elif remaining_life_units < consumed_life_units:
                # Unmount tool
                self.state.set("unmounting")
                yield self.hold(self.tool_type.unmount_time)
                # Remount tool
                self.state.set("mounting")
                yield self.hold(self.tool_type.mount_time)
                # Update life units
                remaining_life_units = total_life_units
            self.state.set("working")
            # Prepare animation
            self.remaining_life_units[tool_type] = remaining_life_units
            self.remaining_life_units_t[tool_type] = self.env.now()
            self.remaining_life_units_next[tool_type] = remaining_life_units - consumed_life_units
            self.remaining_life_units_next_t[tool_type] = self.env.now() + duration
            # Perform process step
            yield self.hold(duration)
            self.state.set("returning")
            job.state.set(operation.produces_product_type.name)
            # Update remaining tool life units
            self.remaining_life_units[tool_type] = remaining_life_units - consumed_life_units
            self.remaining_life_units_t[tool_type] = self.env.now()
            self.remaining_life_units_next[tool_type] = remaining_life_units - consumed_life_units
            self.remaining_life_units_next_t[tool_type] = self.env.now()
            # Place job back to store
            yield self.to_store(self.store_out, job)
    
    def utilization(self):
        waiting = self.state.value.value_duration('waiting')
        mounting = self.state.value.value_duration('mounting')
        unmounting = self.state.value.value_duration('unmounting')
        working = self.state.value.value_duration('working')
        returning = self.state.value.value_duration('returning')

        total = waiting + mounting + unmounting + working + returning

        if total > 0:
            return working / total
        else:
            return 1
    
    def printStatistics(self):
        print(f"       - {self.machine.name} (utilization = {'{:.1f}'.format(self.utilization() * 100)}%)")
    
    def plot(self, legend = False):
        categories = ['Waiting', 'Mounting', 'Unmounting', 'Working', 'Returning']

        waiting = self.state.value.value_duration('waiting')
        mounting = self.state.value.value_duration('mounting')
        unmounting = self.state.value.value_duration('unmounting')
        working = self.state.value.value_duration('working')
        returning = self.state.value.value_duration('returning')

        values = [waiting, mounting, unmounting, working, returning]

        bar_width = 0.15

        # Graph
        for i in range(len(categories)):
            plt.bar(i * bar_width, values[i], width=bar_width, label=categories[i])

        # x Axis
        plt.xticks([])

        # Labels
        plt.xlabel('Machine State')
        plt.ylabel('State Duration')
        plt.title(self.machine.name)

        # Legend
        if legend:
            plt.legend()
