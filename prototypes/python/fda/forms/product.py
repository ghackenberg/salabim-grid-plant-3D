from tkinter import Misc
from tkinter import Label
from tkinter import Entry
from .abstract import AbstractForm
from ..eventbus import EventBus
from ..objects import ProductObject

class ProductForm(AbstractForm[ProductObject]):

    def __init__(self, master: Misc, eventbus: EventBus):
        AbstractForm.__init__(self, master, eventbus, 'product')
        # Add test input field label
        self.testLabel = Label(self.formView, text='Test:')
        self.testLabel.grid(row=1, column=0, padx=5, pady=5)
        # Add test input field entry
        self.testEntry = Entry(self.formView)
        self.testEntry.grid(row=1, column=1, padx=5, pady=5)
    