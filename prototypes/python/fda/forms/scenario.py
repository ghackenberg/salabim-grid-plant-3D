from tkinter import Misc
from .abstract import AbstractForm
from ..objects.scenario import ScenarioObject

class ScenarioForm(AbstractForm[ScenarioObject]):

    def __init__(self, master: Misc=None):
        AbstractForm.__init__(self, master, 'Please select a scenario')
    