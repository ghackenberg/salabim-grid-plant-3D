from .OperationType import *

class ObjectType:
    def __init__(self, name: str) -> None:
        self.name = name

        self.consumingOperationTypes: list[OperationType] = []
        self.producingOperationTypes: list[OperationType] = []

        OBJECT_TYPES.append(self)

OBJECT_TYPES: list[ObjectType] = []