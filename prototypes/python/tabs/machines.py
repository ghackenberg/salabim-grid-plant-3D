from tkinter.ttk import Notebook
from tkinter import Frame

def createMachinesTab(notebook: Notebook):
    frame = Frame(notebook)

    # TODO initialize frame contents

    notebook.add(frame, text='Machines')