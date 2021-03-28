from Validation import Validator
from Strategy import *
from LinkedList import LinkedList
import threading
list1 = LinkedList()
list2 = LinkedList()
lists = [list1, list2]
threadList = []
functions = []
valid = Validator()
context = Context(ReadFromFile())
def Threads(function, *parameter):
    for i in function:
        t = threading.Thread(target=i, args=(parameter))
        threadList.append(t)
        t.start()
    for t in threadList:
        t.join()
    threadList.clear()
    functions.clear()
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
        list1 = context.generateData(list1)
        list2 = context.generateData(list2)
    elif choice == 4:
        print("Вкажіть позицію елемента: ")
        position = valid.isInteger()
        for i in range(len(lists)):
            functions.append(lists[i].remove)
        Threads(functions, position)
    elif choice == 5:
        print("Вкажіть початкову позицію елемента: ")
        fromPos = valid.isInteger()
        print("Вкажіть кінцеву позицію елемента: ")
        toPos = valid.isInteger()
        for i in range(len(lists)):
            functions.append(lists[i].removeFromTo)
        Threads(functions, fromPos, toPos)
    elif choice == 6:
        for i in range(len(lists)):
            functions.append(lists[i].Compression)
        Threads(functions)
    elif choice == 7:
        for i in lists:
            i.Print()
    elif choice == 8:
        break