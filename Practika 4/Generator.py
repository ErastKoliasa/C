from prime import *
def Generator():
    a = 0
    while True:
        a += 1
        if Number(a):
            b = a + 1
            while Number(b) == 0:
                b += 1
            if 2 == (b - a):
                yield a, b