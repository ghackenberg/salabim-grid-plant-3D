from tkinter import Misc
from .abstract import AbstractEditor
from ..eventbus import EventBus
from ..objects import ModelObject
from ..objects import LayoutObject
from ..forms import LayoutForm

class LayoutsEditor(AbstractEditor[LayoutObject, LayoutForm]):

    def __init__(self, master: Misc, eventbus: EventBus, model: ModelObject):
        AbstractEditor.__init__(self, master, eventbus, model, model.layouts, 'layout')
    
    def createObject(self):
        return LayoutObject(f'New layout {len(self.objects) + 1}')
    
    def createForm(self):
        return LayoutForm(self, self.eventbus)
    