from tkinter import Misc
from .abstract import AbstractEditor
from ..objects.product import ProductObject
from ..forms.product import ProductForm

class ProductsEditor(AbstractEditor[ProductObject, ProductForm]):

    def __init__(self, master: Misc=None):
        AbstractEditor.__init__(self, master)
    
    def createObject(self):
        return ProductObject(f'New product type {len(self.objects) + 1}')
    
    def createForm(self):
        return ProductForm(self)
    