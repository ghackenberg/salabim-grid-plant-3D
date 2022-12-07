from typing import TypeVar
from typing import Generic
from tkinter import Frame
from tkinter import Misc
from tkinter import StringVar
from tkinter import Label
from tkinter import Entry
from tkinter import END
from ..eventbus import EventBus
from ..objects import AbstractObject

# The type of object being edited must inherit from abstract object
T = TypeVar('T', bound=AbstractObject)

class AbstractForm(Frame, Generic[T]):

    def __init__(self, master: Misc, eventbus: EventBus, prefix: str):
        Frame.__init__(self, master)
        # Remember the event bus to send and receive messages
        self.eventbus = eventbus
        # Remember event prefix
        self.prefix = prefix
        # Remember object, which is currently displayed in the form
        self.object: AbstractObject = None
        # Configure the grid layout
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        # Label showing the default text or the name of the object
        self.defaultView = Label(self, text=f'Please select {prefix}')
        self.defaultView.grid(row=0, column=0, sticky='')
        # Container for form elements
        self.formView = Frame(self)
        # String variable for the object name
        self.nameVar = StringVar(self.formView)
        self.nameVar.trace('w', lambda a, b, c: self.handleNameChange())
        # Label for text input field for object name
        self.nameLabel = Label(self.formView, text='Name:')
        self.nameLabel.grid(row=0, column=0, padx=5, pady=5)
        # Text input field for changing the name
        self.nameEntry = Entry(self.formView, textvariable=self.nameVar)
        self.nameEntry.grid(row=0, column=1, padx=5, pady=5)
    
    def setObject(self, object: T):
        # Remember the new object, which is shown in the form
        self.object = object
        # Check if a new object is defined or no object is selected
        if object:
            # Switch view
            self.defaultView.grid_forget()
            self.formView.grid(row=0, column=0, sticky='')
            # Update value of name input field
            self.nameVar.set(object.name)
        else:
            # Switch view
            self.formView.grid_forget()
            self.defaultView.grid(row=0, column=0, sticky='')

    def handleNameChange(self):
        # Check if names are different first!
        if self.object.name != self.nameVar.get():
            # Update name
            self.object.name = self.nameVar.get()
            # Propagate event
            self.eventbus.emit(f'{self.prefix}-update', self.object)
