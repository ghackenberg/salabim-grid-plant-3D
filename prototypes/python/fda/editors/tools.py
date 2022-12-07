from tkinter import Misc
from .abstract import AbstractEditor
from ..forms.abstract import AbstractForm
from ..forms.tool import ToolForm

class ToolsEditor(AbstractEditor):

    def __init__(self, master: Misc=None):
        AbstractEditor.__init__(self, master)
    
    def createObject(self) -> str:
        return 'New tool type'
    
    def createForm(self) -> AbstractForm:
        return ToolForm(self)
    