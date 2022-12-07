from tkinter import Misc
from .abstract import AbstractEditor
from ..forms.abstract import AbstractForm
from ..forms.product import ProductForm

class ProductsEditor(AbstractEditor):

    def __init__(self, master: Misc=None):
        AbstractEditor.__init__(self, master)
    
    def createObject(self) -> str:
        return 'New product type'
    
    def createForm(self) -> AbstractForm:
        return ProductForm(self)
    