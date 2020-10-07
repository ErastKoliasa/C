def luckyTickets(n):
   while n % 2 != 0 or n <= 0 or n >= 100:
      print ('Не правильно введено дані')
      n = int(input("Введіть n: "))
   array = [1] * 10 + [0] * (n // 2*9-9)
   for i in range(n // 2-1 ):
       array = [sum(array[x::-1])
       if x < 10 else sum(array[x:x-10:-1])
       for x in range(len(array))]
   return sum([x**2 for x in array])
try:
   n = int(input("Введіть n: "))
except ValueError:
   print("Введіть число")
try:
   print(luckyTickets(n))
except NameError:
    print("Щось пішло не так")
input()
