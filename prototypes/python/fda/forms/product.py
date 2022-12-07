from tkinter import Frame
from tkinter import Label
from tkinter import BOTH

class ProductForm(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)

        self.label = Label(self, text='Please select a product')
        self.label.pack(expand=True, fill=BOTH)
    
    def setProduct(self, product: str):
        if product:
            self.label.config(text=product)
        else:
            self.label.config(text='Please select a product')
    