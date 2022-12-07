from tkinter import Misc
from .abstract import AbstractForm
from ..objects import ToolObject

class ToolForm(AbstractForm[ToolObject]):

    def __init__(self, master: Misc=None):
        AbstractForm.__init__(self, master, 'Please select a tool')
    