from Validation import Validator
valid = Validator()
class GeneratorWithIterator():
    def insert(self, list):
        print("Введіть позицію для вставки:", end='')
        pos = valid.isInteger()
        element = next(iter)
        list.InsertYourValues(pos, element)
        return list