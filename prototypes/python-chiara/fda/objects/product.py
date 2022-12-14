from .abstract import AbstractObject

class ProductObject(AbstractObject):
    
    def __init__(self, name: str):
        AbstractObject.__init__(self, name)
    