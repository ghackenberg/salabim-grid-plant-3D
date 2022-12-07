from tkinter import Misc
from .abstract import AbstractForm

class ToolForm(AbstractForm):

    def __init__(self, master: Misc=None):
        AbstractForm.__init__(self, master, 'Please select a tool')
    