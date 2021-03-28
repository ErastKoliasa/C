from Validation import Validator
valid = Validator()
class ReadFromFile():
    def insert(self, list):
        nameFile = valid.isFileName()
        file = open(nameFile, 'r')
        for line in file:
            obj = line.split()
        obj = valid.isIntList(obj);
        if not obj:
            print("У файлі хибні дані")
            return list
        print("Введіть позицію для вставки:", end='')
        pos = valid.isInteger()
        list.InsertYourValues(pos, obj)
        return list