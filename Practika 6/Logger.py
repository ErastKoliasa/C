from Validation import Validator
valid = Validator()
class Logger:
    def __init__(self, fileName):
        self.fileName = fileName
    @property
    def fileName(self):
        return self._fileName
    @fileName.setter
    def fileName(self, str):
        self._fileName = valid.isFileName(str)
    def printToFile(self, name, dictionary):
        file = open(self.fileName, 'a')
        file.write(name+':'+str(dictionary)+'\n')
        file.close()
