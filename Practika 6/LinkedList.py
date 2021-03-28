from Observer import EventManager
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.eventManager = EventManager()
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
            # return self.head
        else:
            self.head = Node(list[0])
            current = self.head
            for h in range(1, len(list)):
                value = list[h]
                current.next = Node(value)
                current = current.next
        self.eventManager.event("add", {"newList": list, "pos": key, "resultList": self.__str__()})
    def __str__(self):
        result = ''
        if self.head:
            result += '['
            current = self.head
            while current.next:
                result += str(current.data)
                result += ', '
                current = current.next
            result += str(current.data)
            result += ']'
            return result
        else:
            return "empty"
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
    def remove(self, posFrom, posTo):
        if posTo != posFrom:
            posTo -= 1
        current = self.head
        prev = None
        counter = 0
        deletedList = []
        for i in range((posTo - posFrom) + 1):
            if self.head:
                while (counter != posFrom):
                    prev = current
                    current = current.next
                    counter += 1
                if prev:
                    deletedList.append(current.data)
                    prev.next = current.next
                    current=current.next
                else:
                    deletedList.append(self.head.data)
                    self.head = self.head.next
            else:
                posTo = i
                break
        self.eventManager.event("remove",
                                {"deletedList": deletedList, "pos": f"{posFrom}-{posTo}", "resultList": self.__str__()})
