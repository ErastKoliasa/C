from Validation import Validator
from Strategy import *
from LinkedList import LinkedList
from Observer import *
from Logger import Logger

logger = Logger("action.txt")
list = LinkedList()
valid = Validator()
context = Context(ReadFromFile())
list.eventManager.subscribe(Observer("add", logger.printToFile))
list.eventManager.subscribe(Observer("remove", logger.printToFile))

while True:
    try:
        print("1 - Генерувати за допомогою ітератора \n"
              "2 - Зчитувати дані з файла  \n"
              "3 - Генерувати дані \n"
              "4 - Видалити елемент за вказаною позицією\n"
              "5 - Видалити декілька елементів в межах початкової та кінцевої позиції\n"
              "6 - Метод для роботи зі списком\n"
              "7 - Вивести список\n"
              "8 - Вихід\n"
              "Зробіть вибір: ", end='')
        choice = valid.isInteger()
        if choice == 1:
            context._strategy = GeneratorWithIterator()
        elif choice == 2:
            context._strategy = ReadFromFile()
        elif choice == 3:
            list = context.generateData(list)
        elif choice == 4:
            print("Вкажіть позицію елемента: ")
            position = valid.isInteger()
            list.remove(position,position)
        elif choice == 5:
            print("Вкажіть початкову позицію елемента: ")
            fromPos = valid.isInteger()
            print("Вкажіть кінцеву позицію елемента: ")
            toPos = valid.isInteger()
            list.remove(fromPos, toPos)
        elif choice == 6:
            list.Compression()
        elif choice == 7:
            print(list)
        elif choice == 8:
            break
    except:
        print("Помилка")
