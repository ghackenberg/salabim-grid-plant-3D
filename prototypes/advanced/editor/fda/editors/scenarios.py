from tkinter import Misc
from .abstract import AbstractEditor
from ..eventbus import EventBus
from ..objects import ModelObject
from ..objects import ScenarioObject
from ..forms import ScenarioForm

class ScenariosEditor(AbstractEditor[ScenarioObject, ScenarioForm]):

    def __init__(self, master: Misc, eventbus: EventBus, model: ModelObject):
        AbstractEditor.__init__(self, master, eventbus, model, model.scenarios, 'scenario')
    
    def createObject(self):
        return ScenarioObject(f'New scenario {len(self.objects) + 1}')
    
    def createForm(self):
        return ScenarioForm(self, self.eventbus)
    