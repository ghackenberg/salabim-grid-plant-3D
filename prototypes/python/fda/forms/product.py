from tkinter import Misc
from .abstract import AbstractForm
from ..objects import ProductObject

class ProductForm(AbstractForm[ProductObject]):

    def __init__(self, master: Misc=None):
        AbstractForm.__init__(self, master, 'Please select a product')
    