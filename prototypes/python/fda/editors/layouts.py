from tkinter import Misc
from .abstract import AbstractEditor
from ..forms.abstract import AbstractForm
from ..forms.layout import LayoutForm

class LayoutsEditor(AbstractEditor):

    def __init__(self, master: Misc=None):
        AbstractEditor.__init__(self, master)
    
    def createObject(self) -> str:
        return 'New layout'
    
    def createForm(self) -> AbstractForm:
        return LayoutForm(self)
    