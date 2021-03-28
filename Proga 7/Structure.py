import operator
from container import Container
from validation import Validation
valid = Validation()
class Structure:
    def __init__(self):
        self.structure = []
    def __str__(self):
        res = ' '
        for i in self.structure:
            res += str(i)
            res += '\n'
        return res
    def _replaceToString(self):
        result = []
        for j in range(len(self.structure)):
            copy = self.structure[j]
            for i in range(len(Container.parameters())):
                result.append(str(getattr(copy, Container.parameters()[i])))
        return result
    def find(self, parameter):
        stringCopy = self._replaceToString()
        result = []
        for i in range(0, len(stringCopy)):
            if stringCopy[i].find(parameter, 0, len(stringCopy[i])) != -1:
                result.append(stringCopy[i])
        return result
    def sort(self, key):
        for i in Container.parameters():
            if i == key:
                try:
                    self.structure = sorted(self.structure, key=operator.attrgetter(key))
                    return
                except KeyError:
                    print("Немає такого ключа")
    def append(self, line):
        line = line.strip().split()
        for i in self.structure:
            if i.ID == int(line[0]):
                raise ValueError("ID вже зайнятий")
            if i.number == line[1]:
                raise ValueError("Номер вже зайнятий")
        item = Container(*line)
        self.structure.append(item)
    def remove(self, str):
        DeleteLineByID = valid.isInteger(str)
        for i in range(len(self.structure)):
            if self.structure[i].ID == DeleteLineByID:
                del self.structure[i]
                return
    def edit(self, id, attr, value):
        counter = 0
        id = valid.isInteger(id)
        for i in self.structure:
            if i.ID == id:
                setattr(self.structure[counter], attr, value)
            counter += 1
    def ReadingFromFile(self, nameFile):
        file = open(nameFile, mode='r')
        for line in file:
            try:
                self.append(line)
            except ValueError:
                print('Присутній обє\'кт з помилкою')
        file.close()
    def SaveInFile(self, nameFile):
        file = open(nameFile, mode='w')
        for i in range(len(self.structure)):
            file.write(str(self.structure[i]) + '\n')
        file.close()