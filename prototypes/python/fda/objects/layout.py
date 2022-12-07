from .abstract import AbstractObject

class LayoutObject(AbstractObject):
    
    def __init__(self, name: str):
        AbstractObject.__init__(self, name)
    