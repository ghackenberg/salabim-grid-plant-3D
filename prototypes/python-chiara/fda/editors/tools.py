from tkinter import Misc
from .abstract import AbstractEditor
from ..eventbus import EventBus
from ..objects import ModelObject
from ..objects import ToolObject
from ..forms import ToolForm

class ToolsEditor(AbstractEditor[ToolObject, ToolForm]):

    def __init__(self, master: Misc, eventbus: EventBus, model: ModelObject):
        AbstractEditor.__init__(self, master, eventbus, model, model.tools, 'tool')
    
    def createObject(self):
        return ToolObject(f'New tool type {len(self.objects) + 1}')
    
    def createForm(self):
        return ToolForm(self, self.eventbus)
    