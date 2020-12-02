from Structure import *
from validation import Validation
Data = Structure()
valid = Validation()
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
                       "0. Вихід\n"
                       "Введіть: ")
        choice = valid.isInteger(choice)
        if choice == 1:
            fileName = valid.isFileName()
            Data.ReadingFromFile(fileName)
        elif choice == 2:
            line = input("Введіть новий об'єкт: ")
            Data.append(line)
        elif choice == 3:
            Data.edit()
        elif choice == 4:
            Data.remove()
        elif choice == 5:
            key = input("Шукаємо: ")
            Data.find(key)
        elif choice == 6:
            Data.sort()
        elif choice == 7:
            for i in range(len(Data.structure)):
                print(Data.structure[i])
        elif choice == 8:
            fileName = valid.isFileName()
            Data.SaveInFile(fileName)
        else:
            break
    except (ValueError, FileNotFoundError, IndexError, TypeError)as e:
        print(e)
