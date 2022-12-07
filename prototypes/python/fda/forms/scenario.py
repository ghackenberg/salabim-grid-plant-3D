from tkinter import Frame
from tkinter import Misc
from tkinter import Label
from tkinter import BOTH

class ScenarioForm(Frame):

    def __init__(self, master: Misc=None):
        Frame.__init__(self, master)

        self.label = Label(self, text='Please select a scenario')
        self.label.pack(expand=True, fill=BOTH)
    
    def setScenario(self, scenario: str):
        if scenario:
            self.label.config(text=scenario)
        else:
            self.label.config(text='Please select a scenario')
    