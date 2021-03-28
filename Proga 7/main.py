from Structure import *
from validation import Validation
from Memento import Originator, Caretaker
Data = Structure()
valid = Validation()
originator = Originator(Data)
caretaker = Caretaker(originator, "5")
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
            str = input("Введіть назву файла: ")
            fileName = valid.isFileName(str)
            Data.ReadingFromFile(fileName)
            caretaker.backup(Data)
        elif choice == 2:
            line = input("Введіть новий об'єкт: ")
            Data.append(line)
            caretaker.backup(Data)
        elif choice == 3:
            id = input("Введіть ID: ")
            attribute = input("Введіть елемент: ")
            value = input("Введіть значення: ")
            Data.edit(id,attribute,value)
            caretaker.backup(Data)
        elif choice == 4:
            Data.remove()
            caretaker.backup(Data)
        elif choice == 5:
            key = input("Шукаємо: ")
            Data.find(key)
        elif choice == 6:
            key = input(
                "Ключ: 'ID', 'number', 'departureCity', 'arrivalCity', 'departureDate', 'arrivalDate', 'amountOfItems'"
                "\nНемає такого ключа: ")
            Data.sort(key)
            caretaker.backup(Data)
        elif choice == 7:
            for i in range(len(Data.structure)):
                print(Data.structure[i])
        elif choice == 8:
            str = input("Введіть назву файла: ")
            fileName = valid.isFileName(str)
            Data.SaveInFile(fileName)
        elif choice == 9:
            n = input("Введіть n:")
            n = valid.isInteger(n)
            Data = caretaker.undo(n)
        elif choice == 10:
            n = input("Введіть n:")
            n = valid.isInteger(n)
            Data = caretaker.redo(n)
        else:
            break
    except (ValueError, FileNotFoundError, IndexError, TypeError, AttributeError)as e:
        print(e)