from tkinter import Tk
from tkinter import BOTH
from tkinter.ttk import Notebook
from editors.tools import ToolsEditor
from editors.machines import MachinesEditor
from editors.products import ProductsEditor
from editors.scenarios import ScenariosEditor

root = Tk()
root.title('Factory Design Automation (FDA) Tool')
root.attributes('-zoomed', True)

notebook = Notebook(root)

tools = ToolsEditor(notebook)
machines = MachinesEditor(notebook)
products = ProductsEditor(notebook)
scenarios = ScenariosEditor(notebook)

notebook.add(tools, text='Tools')
notebook.add(machines, text='Machines')
notebook.add(products, text='Products')
notebook.add(scenarios, text='Scenarios')
notebook.pack(expand=1, fill=BOTH)

root.mainloop()