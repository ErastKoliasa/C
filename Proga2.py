
from random import randint
min = 1000
max = 10000
def Print(array):
    print(array[0:len(array):1])
def Random(n, array):
    for i in range(0, n):
        Array.insert(len(array), randint(min, max))
def Write(n, array):
    print("Введіть", n, " чотирицифрових елементів")
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
Array = []
try:
    N = int(input("N: "))
except ValueError:
    print("ЦЕ НЕ ЦІЛЕ ЧИСЛО")
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
    Array.clear()
