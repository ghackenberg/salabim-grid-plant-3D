from tkinter import Tk
from tkinter.ttk import Notebook
from tabs.tools import *
from tabs.machines import *
from tabs.products import *
from tabs.scenarios import *

root = Tk()
root.title('Factory Design Automation (FDA) Tool')
root.attributes('-zoomed', True)

notebook = Notebook(root)
createToolsTab(notebook)
createMachinesTab(notebook)
createProductsTab(notebook)
createScenariosTab(notebook)
notebook.pack(expand=1, fill='both')

root.mainloop()