from tkinter import Misc
from .abstract import AbstractForm
from ..eventbus import EventBus
from ..objects import ScenarioObject

class ScenarioForm(AbstractForm[ScenarioObject]):

    def __init__(self, master: Misc, eventbus: EventBus):
        AbstractForm.__init__(self, master, eventbus, 'Please select a scenario')
    