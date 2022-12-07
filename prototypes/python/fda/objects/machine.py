from .abstract import AbstractObject

class MachineObject(AbstractObject):
    
    def __init__(self, name: str):
        AbstractObject.__init__(self, name)
    