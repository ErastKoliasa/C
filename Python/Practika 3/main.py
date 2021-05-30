from LinkedList import *


def ValidateInt():
    try:
        integer = int(input())
        return integer
    except ValueError:
        print("Ви ввели не цілочисельну змінну.")


print("Введіть N - кільість елементів списку:", end='')
N = ValidateInt()
while True:
    list = LinkedList()
    print("\nВиберіть варіант заповнення списку.\n"
          "1: Заповнити випадковими значеннями.\n"
          "2: Ввести значення самостійно.\n"
          "0: Закінчити виконання програми")
    choice = ValidateInt()
    if choice == 1:
        for i in range(N):
            list.InsertRandomValues()

    elif choice == 2:
        print("Введіть ", N, " чотиризначних чисел:")
        for i in range(N):
            K = ValidateInt()
            if (K >= MIN) & (K < MAX):
                list.InsertYourValues(K)
            else:
                print("Ви ввели не 4-х значне число.")
    else:
        break

    list.Compression()
    list.Print()
