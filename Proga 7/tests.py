import unittest
import copy
import datetime
from datetime import date
from Structure import Structure
from validation import Validation
from container import Container
from Memento import Originator, Caretaker
data = Structure()
valid = Validation()
class TestStructure(unittest.TestCase):
    def test_ReadFromFile(self):
        data.ReadingFromFile("Test.txt")
        self.assertEqual(len(data.structure), 5)
    def test_SaveInFile(self):
        copy = Structure()
        data.SaveInFile("Test.txt")
        copy.ReadingFromFile("Test.txt")
        self.assertEqual(len(data.structure), len(copy.structure))
        for i in range(len(data.structure)):
            for j in range(len(data.structure[i].parameters())):
                self.assertEqual(getattr(data.structure[i], data.structure[i].parameters()[j]),
                                 getattr(copy.structure[i], copy.structure[i].parameters()[j]))
        del copy
    def test_replaceToString(self):
        result = data._replaceToString()
        for i in result:
            self.assertIsInstance(i, str)
    def test_find(self):
        result = data.find('Lviv')
        self.assertEqual(len(result), 1)
        result = data.find('0')
        self.assertEqual(len(result), 16)
    def test_append(self):
        size = len(data.structure)
        data.append("1 AA-00000 City City 2000-01-01 2000-01-01 1")
        self.assertEqual(size + 1, len(data.structure))
    def test_remove(self):
        size = len(data.structure)
        data.remove('1')
        self.assertEqual(size - 1, len(data.structure))
    def test_edit(self):
        data.edit('431', 'ID', '23')
        self.assertEqual(getattr(data.structure[4], 'ID'), 23)
    def test_sort(self):
        for i in Container.params():
            data.sort(i)
            for j in range(len(data.structure) - 1):
                self.assertLessEqual(getattr(data.structure[j], i), getattr(data.structure[j + 1], i))
class TestValidation(unittest.TestCase):
    def test_isInteger(self):
        integer = valid.isInteger("23")
        self.assertEqual(integer, 23)
        self.assertRaises(ValueError, valid.isInteger, "-23")
        self.assertRaises(AttributeError, valid.isInteger, 42)
    def test_isFileName(self):
        str = valid.isFileName("Test.txt")
        self.assertEqual(str, "Test.txt")
        self.assertRaises(TypeError, valid.isFileName, "Failed.txxxxxxt")
    def test_isID(self):
        cont = Container("431", "DJ-98346", "Rivne", "Lviv", "2001-02-09", "2010-07-10", "86")
        cont.ID = "99"
        self.assertEqual(cont.ID, 99)
    def test_isNumber(self):
        cont = Container("431", "DJ-98346", "Rivne", "Lviv", "2001-02-09", "2010-07-10", "86")
        cont.number = "AC-12345"
        self.assertEqual(cont.number, "AC-12345")
    def test_isCity(self):
        cont = Container("431", "DJ-98346", "Rivne", "Lviv", "2001-02-09", "2010-07-10", "86")
        cont.departureCity = "Lviv"
        cont.arrivalCity = "Washington"
        self.assertEqual(cont.departureCity, "Lviv")
        self.assertEqual(cont.arrivalCity, "Washington")
    def test_isDate(self):
        cont = Container("431", "DJ-98346", "Rivne", "Lviv", "2001-02-09", "2010-07-10", "86")
        cont.departureDate = "2000-08-30"
        cont.arrivalDate = "2008-10-03"
        self.assertEqual(cont.departureDate, datetime.date(2000, 8, 30))
        self.assertEqual(cont.arrivalDate, datetime.date(2008, 10, 3))
    def test_isAmountOfItems(self):
        cont = Container("431", "DJ-98346", "Rivne", "Lviv", "2001-02-09", "2010-07-10", "86")
        cont.amountOfItems = "1456"
        self.assertEqual(cont.amountOfItems, 1456)
class TestMemento(unittest.TestCase):
    def test_UndoRedo(self):
        data = Structure()
        originator = Originator(data)
        caretaker = Caretaker(originator, "5")
        self.assertEqual(caretaker.maxSize, 5)
        data.ReadingFromFile("Test.txt")
        Copy = copy.deepcopy(data)
        caretaker.backup(data)
        data.remove("2")
        caretaker.backup(data)
        data.remove("84")
        caretaker.backup(data)
        Copy2 = data
        data = caretaker.undo(2)
        for i in range(len(data.structure)):
            for j in range(len(data.structure[i].parameters())):
                self.assertEqual(getattr(data.structure[i], data.structure[i].parameters()[j]),
                                 getattr(Copy.structure[i], Copy.structure[i].parameters()[j]))
        data = caretaker.redo(2)
        for i in range(len(data.structure)):
            for j in range(len(data.structure[i].parameters())):
                self.assertEqual(getattr(data.structure[i], data.structure[i].parameters()[j]),
                                 getattr(Copy2.structure[i], Copy2.structure[i].parameters()[j]))
