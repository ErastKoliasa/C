import re
import datetime
from datetime import datetime
class Validation:
    @staticmethod
    def isID(setter):
        def ID(self, string):
            try:
                if string.isnumeric() & (int(string) >= 0):
                    return setter(self, int(string))
                else:
                    raise ValueError("Не правильні дані в 'ID'")
            except TypeError:
                raise TypeError("Параметер має бути string")
        return ID
    @staticmethod
    def isNumber(setter):
        def Number(self, number):
            result = re.findall('[A-Z]{2}-\d{5}', number)
            if (len(number)) == (8 * len(result)):
                return setter(self, number)
            else:
                raise ValueError("Не правильні дані в 'number'")
        return Number
    @staticmethod
    def isCity(setter):
        def City(self, string):
            result = re.findall('[A-Z][a-z]+', string)
            if len(string) == len(len(string) * result):
                return setter(self, string)
            else:
                raise ValueError("Не правильні дані в 'city'")
        return City
    @staticmethod
    def isDate(setter):
        def Date(self, date):
            str = datetime.strptime(date, "%Y-%m-%d").date()
            return setter(self, str)
        return Date
    @staticmethod
    def isAmountOfItems(setter):
        def AmountOfItems(self, string):
            if string.isnumeric() & (int(string) >= 0):
                return setter(self, int(string))
            else:
                raise ValueError("Не правильні дані в 'amount of items'")
        return AmountOfItems
    def isInteger(self, string):
        if string.isnumeric() & (int(string) >= 0):
            return int(string)
        else:
            raise ValueError("Тип не int")
    def isFileName(self, str):
        result = re.findall('[^\/:*?"<>|]+.txt', str)
        try:
            file = open(str, 'r')
            if result[0] == str:
                file.close()
                return str
        except:
            raise TypeError("Вказано не правильну назву файлу!")