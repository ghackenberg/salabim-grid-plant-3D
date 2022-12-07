from tkinter import Frame
from tkinter import Label
from tkinter import BOTH

class LayoutForm(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)

        self.label = Label(self, text='Please select a layout')
        self.label.pack(expand=True, fill=BOTH)
    
    def setLayout(self, layout: str):
        if layout:
            self.label.config(text=layout)
        else:
            self.label.config(text='Please select a layout')
    