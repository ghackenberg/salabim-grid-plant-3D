from tkinter import Misc
from .abstract import AbstractEditor
from ..objects.scenario import ScenarioObject
from ..forms.scenario import ScenarioForm

class ScenariosEditor(AbstractEditor[ScenarioObject, ScenarioForm]):

    def __init__(self, master: Misc=None):
        AbstractEditor.__init__(self, master)
    
    def createObject(self):
        return ScenarioObject(f'New scenario {len(self.objects) + 1}')
    
    def createForm(self):
        return ScenarioForm(self)
    