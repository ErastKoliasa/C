import operator
from container import Container
from validation import Validation
valid = Validation()
class Structure:
    def __init__(self):
        self.structure = []
    def _replaceToString(self):
        result = []
        for j in range(len(self.structure)):
            copy = self.structure[j]
            for i in range(len(Container.parameters())):
                result.append(str(getattr(copy, Container.parameters()[i])))
        return result
    def find(self, parameter):
        result = self._replaceToString()
        for i in range(0, len(result)):
            if result[i].find(parameter, 0, len(result[i])) != -1:
                print(result[i])
                print(self.structure[i // 7])
    def sort(self):
        while True:
            key = input(
                "Ключ: 'ID', 'number', 'departure city', 'arrival city', 'departure date', 'arrival date', 'amount of items'"
                "\nВведіть ключ: ")
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
    def remove(self):
        DeleteLineByID = input("Введіть ID: ")
        DeleteLineByID = valid.isInteger(DeleteLineByID)
        for i in range(len(self.structure)):
            if self.structure[i].ID == DeleteLineByID:
                del self.structure[i]
                return
    def edit(self):
        self.remove()
        line = input("Введіть відредагований об'єкт: ")
        self.append(line)
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
