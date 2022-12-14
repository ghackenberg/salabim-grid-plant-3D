from tkinter import Misc
from tkinter import Label
from tkinter import Entry
from .abstract import AbstractForm
from ..eventbus import EventBus
from ..objects import ToolObject

class ToolForm(AbstractForm[ToolObject]):

    def __init__(self, master: Misc, eventbus: EventBus):
        AbstractForm.__init__(self, master, eventbus, 'tool')
        # Add test input field label
        self.testLabel = Label(self.formView, text='Test:')
        self.testLabel.grid(row=1, column=0, padx=5, pady=5)
        # Add test input field entry
        self.testEntry = Entry(self.formView)
        self.testEntry.grid(row=1, column=1, padx=5, pady=5)
    
    def setObject(self, object: ToolObject):
        # Call implementation of base class
        super().setObject(object)
        # TODO do other stuff
    