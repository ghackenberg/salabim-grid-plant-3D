from tkinter import Misc
from .abstract import AbstractForm
from ..eventbus import EventBus
from ..objects import LayoutObject

class LayoutForm(AbstractForm[LayoutObject]):

    def __init__(self, master: Misc, eventbus: EventBus):
        AbstractForm.__init__(self, master, eventbus, 'Please select a layout')
    