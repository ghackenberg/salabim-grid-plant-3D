from tkinter import Tk
from tkinter import BOTH
from tkinter.ttk import Notebook
from .editors import ToolsEditor
from .editors import MachinesEditor
from .editors import ProductsEditor
from .editors import LayoutsEditor
from .editors import ScenariosEditor
from .objects import ModelObject

class Application(Tk):
    def __init__(self, model: ModelObject, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()

        self.title('Factory Design Automation (FDA) Tool')
        self.geometry(f'{width}x{height}+0+0')

        notebook = Notebook(self)

        tools = ToolsEditor(model, notebook)
        machines = MachinesEditor(model, notebook)
        products = ProductsEditor(model, notebook)
        layouts = LayoutsEditor(model, notebook)
        scenarios = ScenariosEditor(model, notebook)

        notebook.add(tools, text='Tools')
        notebook.add(machines, text='Machines')
        notebook.add(products, text='Products')
        notebook.add(layouts, text='Layouts')
        notebook.add(scenarios, text='Scenarios')
        notebook.pack(expand=1, fill=BOTH)