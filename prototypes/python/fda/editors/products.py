from tkinter import Misc
from .abstract import AbstractEditor
from ..objects import ModelObject
from ..objects import ProductObject
from ..forms import ProductForm

class ProductsEditor(AbstractEditor[ProductObject, ProductForm]):

    def __init__(self, model: ModelObject, master: Misc=None):
        AbstractEditor.__init__(self, model, model.products, master)
    
    def createObject(self):
        return ProductObject(f'New product type {len(self.objects) + 1}')
    
    def createForm(self):
        return ProductForm(self)
    