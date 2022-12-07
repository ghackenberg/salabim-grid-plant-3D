from tkinter import Misc
from .abstract import AbstractEditor
from ..objects.layout import LayoutObject
from ..forms.layout import LayoutForm

class LayoutsEditor(AbstractEditor):

    def __init__(self, master: Misc=None):
        AbstractEditor.__init__(self, master)
    
    def createObject(self) -> LayoutObject:
        return LayoutObject(f'New layout {len(self.objects) + 1}')
    
    def createForm(self) -> LayoutForm:
        return LayoutForm(self)
    