from Structure import *
from validation import Validation
from Memento import *
Data = Structure()
valid = Validation()
originator = Originator(Data)
maxSize = input("Скільки кроків буде збережено?: ")
caretaker = Caretaker(originator, maxSize)
while True:
    try:
        choice = input("1. Зчитати файл \n"
                       "2. Додати новий об'єкт \n"
                       "3. Редагувати \n"
                       "4. Видалити \n"
                       "5. Пошук \n"
                       "6. Сортувати \n"
                       "7. Вивести файл на екран \n"
                       "8. Зберегти у файл \n"                  
                       "9. Undo \n"
                       "10. Redo \n"
                       "0. Вихід \n"
                       "Введіть: ")
        choice = valid.isInteger(choice)
        if choice == 1:
            fileName = valid.isFileName()
            Data.ReadingFromFile(fileName)
            caretaker.backup(Data)
        elif choice == 2:
            line = input("Введіть новий об'єкт: ")
            Data.append(line)
            caretaker.backup(Data)
        elif choice == 3:
            Data.edit()
            caretaker.backup(Data)
        elif choice == 4:
            Data.remove()
            caretaker.backup(Data)
        elif choice == 5:
            key = input("Шукаємо: ")
            Data.find(key)
        elif choice == 6:
            Data.sort()
            caretaker.backup(Data)
        elif choice == 7:
            for i in range(len(Data.structure)):
                print(Data.structure[i])
        elif choice == 8:
            fileName = valid.isFileName()
            Data.SaveInFile(fileName)
        elif choice == 9:
            n = input("Введіть n: ")
            n = valid.isInteger(n)
            Data = caretaker.undo(n)
        elif choice == 10:
            n = input("Введіть n: ")
            n = valid.isInteger(n)
            Data = caretaker.redo(n)
        else:
            break
    except (ValueError, FileNotFoundError, IndexError, TypeError, AttributeError)as e:
        print(e)