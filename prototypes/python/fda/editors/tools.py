from tkinter import Misc
from .abstract import AbstractEditor
from ..objects import ModelObject
from ..objects import ToolObject
from ..forms import ToolForm

class ToolsEditor(AbstractEditor[ToolObject, ToolForm]):

    def __init__(self, model: ModelObject, master: Misc=None):
        AbstractEditor.__init__(self, model, model.tools, master)
    
    def createObject(self):
        return ToolObject(f'New tool type {len(self.objects) + 1}')
    
    def createForm(self):
        return ToolForm(self)
    