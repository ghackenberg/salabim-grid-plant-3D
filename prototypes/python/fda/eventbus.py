from typing import TypeVar
from typing import Callable
from .objects import AbstractObject

O = TypeVar('O', bound=AbstractObject)

class EventBus:
    
    def __init__(self):
        self.callbacks: dict[str, list[Callable[[str, AbstractObject], None]]] = {}
    
    def on(self, event: str, callback: Callable[[str, AbstractObject], None]):
        if event not in self.callbacks:
            self.callbacks[event] = []
        self.callbacks[event].append(callback)
    
    def off(self, event: str, callback: Callable[[str, AbstractObject], None]):
        if event in self.callbacks:
            self.callbacks[event].remove(callback)

    def emit(self, event: str, object: O):
        if event in self.callbacks:
            for callback in self.callbacks[event]:
                callback(event, object)
