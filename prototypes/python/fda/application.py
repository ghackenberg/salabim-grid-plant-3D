from tkinter import Tk
from tkinter import BOTH
from tkinter.ttk import Notebook
from .editors.tools import ToolsEditor
from .editors.machines import MachinesEditor
from .editors.products import ProductsEditor
from .editors.layouts import LayoutsEditor
from .editors.scenarios import ScenariosEditor

class Application(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        self.title('Factory Design Automation (FDA) Tool')
        self.attributes('-zoomed', True)

        notebook = Notebook(self)

        tools = ToolsEditor(notebook)
        machines = MachinesEditor(notebook)
        products = ProductsEditor(notebook)
        layouts = LayoutsEditor(notebook)
        scenarios = ScenariosEditor(notebook)

        notebook.add(tools, text='Tools')
        notebook.add(machines, text='Machines')
        notebook.add(products, text='Products')
        notebook.add(layouts, text='Layouts')
        notebook.add(scenarios, text='Scenarios')
        notebook.pack(expand=1, fill=BOTH)