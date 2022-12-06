from tkinter.ttk import Notebook
from tkinter import Frame

def createScenariosTab(notebook: Notebook):
    frame = Frame(notebook)

    # TODO initialize frame contents

    notebook.add(frame, text='Scenarios')