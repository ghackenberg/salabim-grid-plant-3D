from typing import TypeVar
from tkinter import Frame
from tkinter import Misc
from tkinter import Label
from tkinter import BOTH
from ..objects.abstract import AbstractObject

T = TypeVar('T', bound=AbstractObject)

class AbstractForm(Frame):

    def __init__(self, master: Misc, default: str):
        Frame.__init__(self, master)

        self.default = default

        self.object: AbstractObject = None

        self.label = Label(self, text=default)
        self.label.pack(expand=True, fill=BOTH)
    
    def setObject(self, object: T):
        self.object = object
        if object:
            self.label.config(text=object.getName())
        else:
            self.label.config(text=self.default)
