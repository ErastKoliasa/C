from validation import Validation
class Container:
    @staticmethod
    def parameters():
        return ['ID', 'number', 'departureCity', 'arrivalCity', 'departureDate', 'arrivalDate', 'amountOfItems']
    def __init__(self, *args):
        for i in range(len(Container.parameters())):
            setattr(self, Container.parameters()[i], args[i])
    def __str__(self):
        result = ' '
        for i in range(len(Container.parameters())):
            result += str(getattr(self, Container.parameters()[i]))
            result += ' '
        result.strip()
        return result
    @property
    def ID(self):
        return self._ID
    @ID.setter
    @Validation.isID
    def ID(self, value):
        self._ID = value
    @property
    def number(self):
        return self._number
    @number.setter
    @Validation.isNumber
    def number(self, value):
        self._number = value
    @property
    def departureCity(self):
        return self._departureCity
    @departureCity.setter
    @Validation.isCity
    def departureCity(self, value):
        self._departureCity = value
    @property
    def arrivalCity(self):
        return self._arrivalCity
    @arrivalCity.setter
    @Validation.isCity
    def arrivalCity(self, value):
        self._arrivalCity = value
    @property
    def departureDate(self):
        return self._departureDate
    @departureDate.setter
    @Validation.isDate
    def departureDate(self, value):
        if hasattr(self, "_arrivalDate"):
            if not (self.arrivalDate >= value):
                raise ValueError
        self._departureDate = value
    @property
    def arrivalDate(self):
        return self._arrivalDate
    @arrivalDate.setter
    @Validation.isDate
    def arrivalDate(self, value):
        if hasattr(self, "_departureDate"):
            if not (self.departureDate <= value):
                raise ValueError
        self._arrivalDate = value
    @property
    def amountOfItems(self):
        return self._amountOfItems
    @amountOfItems.setter
    @Validation.isAmountOfItems
    def amountOfItems(self, value):
        self._amountOfItems = value

        
