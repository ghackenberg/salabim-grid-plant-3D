from .abstract import AbstractObject

class ToolObject(AbstractObject):
    
    def __init__(self, name: str):
        AbstractObject.__init__(self, name)
    