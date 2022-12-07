from tkinter import Misc
from .abstract import AbstractEditor
from ..forms.abstract import AbstractForm
from ..forms.scenario import ScenarioForm

class ScenariosEditor(AbstractEditor):

    def __init__(self, master: Misc=None):
        AbstractEditor.__init__(self, master)
    
    def createObject(self) -> str:
        return 'New scenario'
    
    def createForm(self) -> AbstractForm:
        return ScenarioForm(self)
    