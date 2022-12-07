from tkinter import Misc
from .abstract import AbstractEditor
from ..objects import ModelObject
from ..objects import LayoutObject
from ..forms import LayoutForm

class LayoutsEditor(AbstractEditor[LayoutObject, LayoutForm]):

    def __init__(self, model: ModelObject, master: Misc=None):
        AbstractEditor.__init__(self, model, model.layouts, master)
    
    def createObject(self):
        return LayoutObject(f'New layout {len(self.objects) + 1}')
    
    def createForm(self):
        return LayoutForm(self)
    