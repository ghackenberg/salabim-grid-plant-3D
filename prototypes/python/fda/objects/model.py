from .abstract import AbstractObject
from .layout import LayoutObject
from .machine import MachineObject
from .product import ProductObject
from .scenario import ScenarioObject
from .tool import ToolObject

class ModelObject(AbstractObject):
    
    def __init__(self, name: str):
        AbstractObject.__init__(self, name)

        self.tools: list[ToolObject] = []
        self.machines: list[MachineObject] = []
        self.products: list[ProductObject] = []
        self.layouts: list[LayoutObject] = []
        self.scenarios: list[ScenarioObject] = []
    