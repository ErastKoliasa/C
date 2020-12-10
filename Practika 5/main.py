from Validation import Validator
from Strategy import *
from LinkedList import LinkedList
list = LinkedList()
valid = Validator()
context = Context(ReadFromFile())
while True:
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
        list = context.generateData()
    elif choice == 4:
        print("Вкажіть позицію елемента: ")
        position = valid.isInteger()
        list.remove(position)
    elif choice == 5:
        print("Вкажіть початкову позицію елемента: ")
        fromPos = valid.isInteger()
        print("Вкажіть кінцеву позицію елемента: ")
        toPos = valid.isInteger()
        list.removeFromTo(fromPos, toPos)
    elif choice == 6:
        list.Compression()
    elif choice == 7:
        list.Print()
    elif choice == 8:
        break