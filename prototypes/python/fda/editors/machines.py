from tkinter import Misc
from .abstract import AbstractEditor
from ..objects.machine import MachineObject
from ..forms.machine import MachineForm

class MachinesEditor(AbstractEditor[MachineObject, MachineForm]):

    def __init__(self, master: Misc=None):
        AbstractEditor.__init__(self, master)
    
    def createObject(self):
        return MachineObject(f'New machine type {len(self.objects) + 1}')
    
    def createForm(self):
        return MachineForm(self)
    