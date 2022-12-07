from tkinter import Misc
from .abstract import AbstractEditor
from ..forms.abstract import AbstractForm
from ..forms.machine import MachineForm

class MachinesEditor(AbstractEditor):

    def __init__(self, master: Misc=None):
        AbstractEditor.__init__(self, master)
    
    def createObject(self) -> str:
        return 'New machine type'
    
    def createForm(self) -> AbstractForm:
        return MachineForm(self)
    