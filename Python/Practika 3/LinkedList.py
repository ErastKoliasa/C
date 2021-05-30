from random import randint

MIN = 1000
MAX = 10000  # не хардкод, бо в умові лише 4-х значні


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def InsertYourValues(self, value):
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(value)
        else:
            self.head = Node(value)

    def InsertRandomValues(self):
        self.InsertYourValues(randint(MIN, MAX))

    def Print(self):
        if self.head:
            print('[', end='')
            current = self.head
            while current.next:
                print(current.data, ", ", end='')
                current = current.next
            print(current.data, ']')
        else:
            print("Список порожній")

    def Compression(self):
        counter = 0
        current = self.head
        prev = None
        while current:
            IntegerToString = str(current.data)
            if not ((IntegerToString[0] == IntegerToString[3]) & (IntegerToString[1] == IntegerToString[2])) | (
                    IntegerToString[0] == IntegerToString[2]) & (IntegerToString[1] == IntegerToString[3]):
                counter += 1
                if prev is None:
                    self.head = self.head.next
                    current = self.head
                else:
                    prev.next = current.next
                    current = prev.next
            else:
                prev = current
                current = current.next
        for i in range(counter):
            self.InsertYourValues(0)
