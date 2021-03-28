import re
class Validator:
    def isFileName(self):
        while True:
            str = input("Вкажіть файл: ")
            result = re.findall('[^\/:*?"<>|]+.txt', str)
            try:
                file = open(str, 'r')
                if result[0] == str:
                    file.close()
                    return str
            except:
                print("Не правильна назва файла!")
    def isInteger(self):
        while True:
            integer = input()
            if integer.isnumeric():
                return int(integer)
            print("Це не число")
            print("Введіть знову: ", end='')
    def isIntList(self, list):
        result = True
        for i in range(len(list)):
            if not list[i].isnumeric():
                result = False
        if result:
            return list
        else:
            return False