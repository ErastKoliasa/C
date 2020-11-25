def Matrix(n):
    for i in range(0, n):
        matrix = []
        for j in range(0, n - i):
            matrix.insert(len(matrix), i + j + 1)
        for j in range(n - i, n):
            matrix.insert(len(matrix), 0)
        print(matrix)
while True:
    choice = int(input("Утворити матрицю натисніть - 1\n"
                       "Вийти натисніть - 0\n"))
    if choice == 1:
        try:
            N = int(input("N: "))
            Matrix(N)
        except ValueError:
            print("ЦЕ НЕ ЦІЛЕ ЧИСЛО!")
    else:
        break