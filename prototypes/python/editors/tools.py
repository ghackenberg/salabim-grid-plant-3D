from tkinter import Frame
from tkinter import Button
from tkinter import Variable
from tkinter import Listbox
from tkinter import Label
from tkinter import LEFT
from tkinter import Y
from tkinter import BOTH
from tkinter import END

class ToolsEditor(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)

        # Container for left sidebar

        left = Frame(self)
        left.pack(side=LEFT, fill=Y)

        # Container for horizontal alignment of buttons

        buttons = Frame(left)
        buttons.pack()

        # Button for adding tools

        def handleButtonAddClick():
            listbox.insert(0, 'New Tool Type')
            listbox.selection_clear(0, END)
            listbox.selection_set(0)
            listbox.event_generate("<<ListboxSelect>>")

        buttonAdd = Button(buttons, text='Add', command=handleButtonAddClick)
        buttonAdd.pack(side=LEFT)

        # Button for removing tools
        
        def handleButtonRemoveClick():
            if listbox.curselection():
                listbox.delete(listbox.curselection())
                label.config(text='Please select a tool type')

        buttonRemove = Button(buttons, text='Remove', command=handleButtonRemoveClick)
        buttonRemove.pack(side=LEFT)

        # List of tools
        
        def handleListboxSelect(event):
            index = listbox.curselection()
            tool = listbox.get(index)
            label.config(text=tool)

        items = ('Tool Type A', 'Tool Type B', 'Tool Type C')

        variable = Variable(value=items)

        listbox = Listbox(left, listvariable=variable)
        listbox.pack(expand=True, fill=Y)
        listbox.bind('<<ListboxSelect>>', handleListboxSelect)

        # Right

        right = Frame(self)
        right.pack(fill=BOTH)

        # Label

        label = Label(right, text='Please select a tool type')
        label.pack()