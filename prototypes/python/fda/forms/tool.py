from tkinter import Frame
from tkinter import Misc
from tkinter import Label
from tkinter import BOTH

class ToolForm(Frame):

    def __init__(self, master: Misc=None):
        Frame.__init__(self, master)

        self.label = Label(self, text='Please select a tool')
        self.label.pack(expand=True, fill=BOTH)

    def setTool(self, tool: str):
        if tool:
            self.label.config(text=tool)
        else:
            self.label.config(text='Please select a tool')
    