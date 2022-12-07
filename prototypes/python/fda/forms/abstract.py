from typing import TypeVar
from typing import Generic
from tkinter import Frame
from tkinter import Misc
from tkinter import Label
from tkinter import BOTH
from ..objects import AbstractObject

# The type of object being edited must inherit from abstract object
T = TypeVar('T', bound=AbstractObject)

class AbstractForm(Frame, Generic[T]):

    def __init__(self, master: Misc, default: str):
        Frame.__init__(self, master)
        # Remember default text to show when no object is selected
        self.default = default
        # Remember object, which is currently displayed in the form
        self.object: AbstractObject = None
        # Label showing the default text or the name of the object
        self.label = Label(self, text=default)
        self.label.pack(expand=True, fill=BOTH)
    
    def setObject(self, object: T):
        # Remember the new object, which is shown in the form
        self.object = object
        # Check if a new object is defined or no object is selected
        if object:
            # Show the name of the selected object in the label
            self.label.config(text=object.name)
        else:
            # Show the default text in the label
            self.label.config(text=self.default)
