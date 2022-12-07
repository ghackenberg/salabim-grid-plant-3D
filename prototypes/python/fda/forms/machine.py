from tkinter import Misc
from .abstract import AbstractForm
from ..objects import MachineObject

class MachineForm(AbstractForm[MachineObject]):

    def __init__(self, master: Misc=None):
        AbstractForm.__init__(self, master, 'Please select a machine')
    