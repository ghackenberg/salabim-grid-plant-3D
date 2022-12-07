from tkinter import Misc
from .abstract import AbstractEditor
from ..eventbus import EventBus
from ..objects import ModelObject
from ..objects import MachineObject
from ..forms import MachineForm

class MachinesEditor(AbstractEditor[MachineObject, MachineForm]):

    def __init__(self, master: Misc, eventbus: EventBus, model: ModelObject):
        AbstractEditor.__init__(self, master, eventbus, model, model.machines)
    
    def createObject(self):
        return MachineObject(f'New machine type {len(self.objects) + 1}')
    
    def createForm(self):
        return MachineForm(self, self.eventbus)
    