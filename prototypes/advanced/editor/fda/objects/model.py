from .abstract import AbstractObject
from .layout import LayoutObject
from .machine import MachineObject
from .product import ProductObject
from .scenario import ScenarioObject
from .tool import ToolObject

class ModelObject(AbstractObject):
    
    def __init__(self, name: str):
        AbstractObject.__init__(self, name)
        # Define list of tools
        self.tools: list[ToolObject] = [ToolObject('New tool type 1')]
        # Define list of machines
        self.machines: list[MachineObject] = [MachineObject('New machine type 1')]
        # Define list of products
        self.products: list[ProductObject] = [ProductObject('New product type 1')]
        # Define list of layouts
        self.layouts: list[LayoutObject] = [LayoutObject('New layout 1')]
        # Define list of scenarios
        self.scenarios: list[ScenarioObject] = [ScenarioObject('New scenario 1')]
    