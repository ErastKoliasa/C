class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def InsertYourValues(self, key, list):
        counter = 0
        if self.head:
            current = self.head
            while current.next:
                if key != counter:
                    current = current.next
                else:
                    break
                counter += 1
            BrokenLink = current.next
            for h in range(len(list)):
                value = list[h]
                current.next = Node(value)
                current = current.next
            current.next = BrokenLink
            return self.head
        else:
            self.head = Node(list[0])
            current = self.head
            for h in range(1, len(list)):
                value = list[h]
                current.next = Node(value)
                current = current.next
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
            if len(IntegerToString) == 4:
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
            else:
                current = current.next
        current = self.head
        while current.next:
            current = current.next
        for i in range(counter):
            current.next = Node(0)
            current = current.next
    def remove(self, pos):
        current = self.head
        prev = None
        counter = 0
        if current:
            while (counter != pos):
                prev = current
                current = current.next
                counter += 1
            if prev:
                prev.next = current.next
            else:
                self.head = self.head.next
        return current
    def removeFromTo(self, posFrom, posTo):
        for i in range(posTo - posFrom):
            self.remove(posFrom)
