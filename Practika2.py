from random import randint
import random
min = 1000
max = 10000
def Print(array):
    print(array[0:len(array):1])
def Random(n, array):
    for i in range(0, n):
        Array.insert(len(array), randint(min, max))
def Write(n, array):
    print("Введіть", n, " чотирицифрових елементів.")
    for i in range(0, n):
        try:
            elem = int(input())
        except ValueError:
            print("ЦЕ НЕ ЧИСЛО!")
        if (elem < max) & (elem >= min):
            array.insert(len(array), elem)
        else:
            print("ЦЕ НЕ ЧОТИРИЦИФРОВЕ ЧИСЛО!")
def Compression(n, array):
    for i in range(0, n):
        inttostr = str(array[i])
        if (inttostr[0] == inttostr[2]) & (inttostr[1] == inttostr[3]):
            array[i] = 0
        elif (inttostr[0] == inttostr[3]) & (inttostr[1] == inttostr[2]):
            array[i] = 0
    for i in range(0, len(array)):
        if array[i] == 0:
            array.remove(0)
            array.insert(len(array), 0)
    return array
def InputInt(message):
    try:
        result = int(input(message))
    except ValueError:
        print("ЦЕ НЕ ЦІЛЕ ЧИСЛО")
    return result
def Sort(array):
    if len(array) <= 1:
        return array
    else:
        h = array[0]
        rozmir1 = []
        rozmir2 = []
        rozmir3 = []
        for n in array:
            if n < h:
                rozmir1.append(n)
            elif n > h:
                rozmir2.append(n)
            else:
                rozmir3.append(n)
        return Sort(rozmir1)  + rozmir3 + Sort(rozmir2)
def BinarySearch(n, array, k):
    counter = 0
    start = 0
    stop = len(array)
    j = 1
    result = []
    for i in range(0, n):
        middle = (start + stop) // 2
        counter += 1
        print("Чи К є більше/менше/рівне елементу. Кількість операцій = ", counter)
        if array[middle] == k:
            while (middle - j >= 0) & (array[middle - j] == k):
                middle = middle - j
                counter += 1
                print("Повернення до елементів = К. Кількість операцій = ", counter)
            while array[middle] == k:
                result.insert(len(array), middle)
                counter += 1
                print("Запис елементів = К. Кількість операцій = ", counter)
                middle += 1
                if middle == len(array):
                    counter += 1
                    print("Повернення результату. Кількість операцій = ", counter)
                    return result
            counter += 1
            print("Повернення результату. Кількість операцій = ", counter)
            return result
        elif (middle + 1 == stop) & (start == middle) & (k != array[middle]):
            return []
        elif array[middle] < k:
            start = middle
            counter += 1
            print("Елемент в масиві менший від К. Кількість операцій на даному моменті = ", counter)
        elif array[middle] > k:
            stop = middle
            counter += 1
            print("Елемент в масиві більший від К. Кількість операцій на даному моменті = ", counter)
Array = []
N = InputInt("N: ")
while True:
    choice = int(input("Щоб заповнити випадковими значеннями натисніть - 1 \n"
                       "Щоб ввести значення самостійно натисніть - 2\n"
                       "Щоб закінчити роботу програми натисніть - 0\n"))
    if choice == 1:
        Random(N, Array)
    elif choice == 2:
        Write(N, Array)
    else:
        break
    print("Масив: ")
    Print(Array)
    print("Результуючий масив: ")
    Print(Compression(N, Array))
    K = InputInt("К: ")
    Array = Sort(Array)
    print("Відсортований масив: ")
    Print(Array)
    Result = BinarySearch(N, Array, K)
    if len(Result):
        print(Result[0:len(Result):1])
    else:
        print("Немає такого елементу")
    Array.clear()