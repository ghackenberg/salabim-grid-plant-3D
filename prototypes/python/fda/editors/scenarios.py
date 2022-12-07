from tkinter import Misc
from .abstract import AbstractEditor
from ..objects import ModelObject
from ..objects import ScenarioObject
from ..forms import ScenarioForm

class ScenariosEditor(AbstractEditor[ScenarioObject, ScenarioForm]):

    def __init__(self, model: ModelObject, master: Misc=None):
        AbstractEditor.__init__(self, model, model.scenarios, master)
    
    def createObject(self):
        return ScenarioObject(f'New scenario {len(self.objects) + 1}')
    
    def createForm(self):
        return ScenarioForm(self)
    