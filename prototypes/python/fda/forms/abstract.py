from tkinter import Frame
from tkinter import Misc
from tkinter import Label
from tkinter import BOTH

class AbstractForm(Frame):

    def __init__(self, master: Misc, default: str):
        Frame.__init__(self, master)

        self.default = default

        self.label = Label(self, text=default)
        self.label.pack(expand=True, fill=BOTH)
    
    def setObject(self, object):
        if object:
            self.label.config(text=object)
        else:
            self.label.config(text=self.default)
