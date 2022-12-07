from tkinter import Misc
from .abstract import AbstractEditor
from ..eventbus import EventBus
from ..objects import ModelObject
from ..objects import ProductObject
from ..forms import ProductForm

class ProductsEditor(AbstractEditor[ProductObject, ProductForm]):

    def __init__(self, master: Misc, eventbus: EventBus, model: ModelObject):
        AbstractEditor.__init__(self, master, eventbus, model, model.products, 'product')
    
    def createObject(self):
        return ProductObject(f'New product type {len(self.objects) + 1}')
    
    def createForm(self):
        return ProductForm(self, self.eventbus)
    