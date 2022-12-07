from tkinter import Frame
from tkinter import Label
from tkinter import BOTH

class MachineForm(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)

        self.label = Label(self, text='Please select a machine')
        self.label.pack(expand=True, fill=BOTH)
    
    def setMachine(self, machine: str):
        if machine:
            self.label.config(text=machine)
        else:
            self.label.config(text='Please select a machine')
    