from tkinter import Misc
from .abstract import AbstractEditor
from ..objects.scenario import ScenarioObject
from ..forms.scenario import ScenarioForm

class ScenariosEditor(AbstractEditor):

    def __init__(self, master: Misc=None):
        AbstractEditor.__init__(self, master)
    
    def createObject(self) -> ScenarioObject:
        return ScenarioObject(f'New scenario {len(self.objects) + 1}')
    
    def createForm(self) -> ScenarioForm:
        return ScenarioForm(self)
    