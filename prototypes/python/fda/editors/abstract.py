from abc import abstractmethod
from typing import TypeVar
from typing import Generic
from tkinter import Frame
from tkinter import Misc
from tkinter import Button
from tkinter import Variable
from tkinter import Listbox
from tkinter import Event
from tkinter import LEFT
from tkinter import Y
from tkinter import END
from tkinter import BOTH
from ..eventbus import EventBus
from ..objects import AbstractObject
from ..objects import ModelObject
from ..forms import AbstractForm

O = TypeVar('O', bound=AbstractObject)
F = TypeVar('F', bound=AbstractForm)

class AbstractEditor(Frame, Generic[O, F]):

    def __init__(self, master: Misc, eventbus: EventBus, model: ModelObject, objects: list[O], prefix: str):
        Frame.__init__(self, master)

        # Handle object updates
        eventbus.on(f'{prefix}-update', self.handleObjectUpdate)

        # Remember the event bus
        self.eventbus = eventbus
        # Remember the model that is being edited
        self.model = model
        # Remember the objects of the model that are mainly edited
        self.objects = objects
        # Remember event prefix
        self.prefix = prefix

        # Container for left sidebar
        self.left = Frame(self)
        self.left.pack(side=LEFT, fill=Y)
        # Container for horizontal alignment of buttons
        self.buttons = Frame(self.left)
        self.buttons.pack()
        # Button for adding objects
        self.buttonAdd = Button(self.buttons, text='Add', command=self.handleButtonAddClick)
        self.buttonAdd.pack(side=LEFT)
        # Button for removing objects
        self.buttonRemove = Button(self.buttons, text='Remove', command=self.handleButtonRemoveClick)
        self.buttonRemove.pack(side=LEFT)
        # Names of the objects
        self.variable = Variable(value=list(map(lambda x: x.name, objects)))
        # List of object names
        self.listbox = Listbox(self.left, listvariable=self.variable)
        self.listbox.pack(expand=True, fill=Y)
        self.listbox.bind('<<ListboxSelect>>', self.handleListboxSelect)

        # Right
        self.right: F = self.createForm()
        self.right.pack(expand=True, fill=BOTH)
    
    def handleObjectUpdate(self, event: str, object: O):
        # Remember previous selection
        selection = self.listbox.curselection()
        # Determine index of object
        index = self.objects.index(object)
        # Dekete old object name
        self.listbox.delete(index)
        # Insert new object name
        self.listbox.insert(index, object.name)
        # Restore selection (if necessary)
        if selection and index == selection[0]:
            self.listbox.selection_clear(0, END)
            self.listbox.selection_set(index)

    def handleButtonAddClick(self):
        # Create the new object
        object: O = self.createObject()
        # Remember the new object
        self.objects.insert(0, object)
        # List and select the new object
        self.listbox.insert(0, object.name)
        self.listbox.selection_clear(0, END)
        self.listbox.selection_set(0)
        self.listbox.event_generate("<<ListboxSelect>>")
        # Emit event
        self.eventbus.emit(f'{self.prefix}-create', object)
        
    def handleButtonRemoveClick(self):
        # Get selection index
        index = self.listbox.curselection()
        # Check selection index
        if index:
            # Get selected object
            object = self.objects[index[0]]
            # Delete the object
            self.objects.remove(object)
            # Unlist the object
            self.listbox.delete(index[0])
            # Unset the object
            self.right.setObject(None)
            # Emit event
            self.eventbus.emit(f'{self.prefix}-delete', object)
        
    def handleListboxSelect(self, event: Event):
        # Get selection index
        index = self.listbox.curselection()
        # Check selection index
        if index:
            # Get selected object
            object = self.objects[index[0]]
            # Set selected object
            self.right.setObject(object)

    @abstractmethod
    def createObject(self) -> O:
        pass

    @abstractmethod
    def createForm(self) -> F:
        pass
