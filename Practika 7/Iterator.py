from prime import *
class Iterator:
    def __init__(self, start=1):
        self.num = start
    def __iter__(self):
        return self
    def __next__(self):
        a = self.num
        while True:
            a += 1
            if PrimeNumber(a):
                b = a + 1
                while PrimeNumber(b) == 0:
                    b += 1
                if 2 == (b - a):
                    self.num = b - 1
                    return a, b