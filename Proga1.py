
try:
    n = int(input('Введіть n (n - діапазон (2,...,n)): '))
except ValueError:
    print("Потрібно ввести число")
list = []
def prime(n):
    # перевіряємо чи n є просте
    # перевіряємо чи n ціле додатнє число
    n = abs(int(n))
    # 0 і 1 не є простими числами
    while n < 2:
        return False
    # 2 - єдине парне просте число
    if n == 2:
        return True
    # діапазон починаємо з 2 і продовжуємо до  n
    while not n & 1:
       return False
    for x in range(2, n):
        while n % x == 0:
            return False
    return True
try:
    for i in range(2, n):
        if prime(i):
            list.append(i)
except NameError:
    print("Щось пішло не так")
for i in range(2, len(list)):
    if list[i] - list[i - 1] == 2:
        print(list[i - 1], list[i])
input('Нажміть любу клавішу щоб закрити програму')
