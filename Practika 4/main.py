from Generator import *
from Iterator import *
def IntInput(str):
    try:
        integer = int(input(str))
        return integer
    except ValueError:
        print("Це не число")
        return False
def GenerateNumbers(GenOrIter, n):
    for i in range(n):
        print(next(GenOrIter), end=' ')
    print('\n')
iter = Iterator()
gen = Generator()
while True:
    choice = IntInput("1 - Ітератор\n"
                      "2 - Генератор\n"
                      "0 - Вихід\n"
                      "Введіть число: ")
    N = IntInput("Введіть кількість пар: ")
    if choice == 1:
        GenerateNumbers(iter, N)
    elif choice == 2:
        GenerateNumbers(gen, N)
    else:
        break