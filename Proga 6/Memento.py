from Structure import *
import copy
from validation import Validation
valid = Validation()
class ConcreteMemento():
    def __init__(self, state):
        self._state = state
    def get_state(self):
        return self._state
class Originator():
    def __init__(self, state):
        self._state = state
    def save(self, newData):
        return ConcreteMemento(newData)
class Caretaker():
    def __init__(self, originator, maxSize):
        self._mementos = []
        self._originator = originator
        self.maxSize = maxSize
        self.current = 0
    @property
    def maxSize(self):
        return self._maxSize
    @maxSize.setter
    def maxSize(self, str):
        self._maxSize=valid.isInteger(str)
    def backup(self, data):
        Data = copy.deepcopy(data)
        if len(self._mementos) == self.maxSize:
            del self._mementos[0]
        if self.current != len(self._mementos):
            for i in range(self.current, len(self._mementos)):
                del self._mementos[i]
        self._mementos.append(self._originator.save(Data))
        self.current += 1
    def undo(self, n):
        if not len(self._mementos):
            return
        try:
            self.current -= n
            if self.current < 0:
                raise IndexError("Немає історії")
            return copy.deepcopy(self._mementos[self.current - 1]._state)
        except:
            print("Щось пішло не так")
    def redo(self, n):
        if not len(self._mementos):
            return
        try:
            self.current += n
            if self.current > len(self._mementos):
                raise IndexError("Індекс завеликий" )
            return copy.deepcopy(self._mementos[self.current - 1]._state)
        except:
            print("Щось пішло не так")