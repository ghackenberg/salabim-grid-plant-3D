from tkinter import Tk
from tkinter import BOTH
from tkinter.ttk import Notebook
from .eventbus import EventBus
from .editors import ToolsEditor
from .editors import MachinesEditor
from .editors import ProductsEditor
from .editors import LayoutsEditor
from .editors import ScenariosEditor
from .objects import ModelObject

class Application(Tk):
    def __init__(self, model: ModelObject, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        # Set window title
        self.title('Factory Design Automation (FDA) Tool')

        # Get width and height of screen
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()

        # Maximize window on start
        self.geometry(f'{width}x{height}+0+0')

        # Create event bus
        eventbus = EventBus()
        eventbus.on('tool-create', lambda event, object: print(event, object.name))
        eventbus.on('tool-update', lambda event, object: print(event, object.name))
        eventbus.on('tool-delete', lambda event, object: print(event, object.name))

        # Create tab view
        notebook = Notebook(self)

        # Create tab contents
        tools = ToolsEditor(notebook, eventbus, model)
        machines = MachinesEditor(notebook, eventbus, model)
        products = ProductsEditor(notebook, eventbus, model)
        layouts = LayoutsEditor(notebook, eventbus, model)
        scenarios = ScenariosEditor(notebook, eventbus, model)

        # Add tab contents to tab view
        notebook.add(tools, text='Tools')
        notebook.add(machines, text='Machines')
        notebook.add(products, text='Products')
        notebook.add(layouts, text='Layouts')
        notebook.add(scenarios, text='Scenarios')

        # Show tab view
        notebook.pack(expand=1, fill=BOTH)