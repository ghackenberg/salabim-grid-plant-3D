from fda import ModelObject
from fda import Application

# Create empty model
model = ModelObject('New model')

# Start GUI application with empty model
application = Application(model)
application.mainloop()