from Validation import Validator
from LinkedList import LinkedList
from Generator import GeneratorWithIterator
from readFile import ReadFromFile
valid = Validator()
class Context():
    def __init__(self, Strategy):
        self._strategy = Strategy
    @property
    def strategy(self):
        return self._strategy
    @strategy.setter
    def strategy(self, Strategy):
        self._strategy = Strategy
    def generateData(self,list):
        return self._strategy.insert(list)