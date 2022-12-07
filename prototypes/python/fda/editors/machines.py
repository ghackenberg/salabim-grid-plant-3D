from tkinter import Misc
from .abstract import AbstractEditor
from ..objects import ModelObject
from ..objects import MachineObject
from ..forms import MachineForm

class MachinesEditor(AbstractEditor[MachineObject, MachineForm]):

    def __init__(self, model: ModelObject, master: Misc=None):
        AbstractEditor.__init__(self, model, model.machines, master)
    
    def createObject(self):
        return MachineObject(f'New machine type {len(self.objects) + 1}')
    
    def createForm(self):
        return MachineForm(self)
    