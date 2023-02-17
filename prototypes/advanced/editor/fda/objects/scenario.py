from .abstract import AbstractObject

class ScenarioObject(AbstractObject):
    
    def __init__(self, name: str):
        AbstractObject.__init__(self, name)
    