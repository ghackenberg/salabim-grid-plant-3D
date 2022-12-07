from tkinter import Misc
from .abstract import AbstractForm
from ..objects import LayoutObject

class LayoutForm(AbstractForm[LayoutObject]):

    def __init__(self, master: Misc=None):
        AbstractForm.__init__(self, master, 'Please select a layout')
    