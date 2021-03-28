class EventManager:
    def __init__(self):
        self._observers = []
    def subscribe(self, Observer):
        if not Observer in self._observers:
            self._observers.append(Observer)
    def event(self, operation, action):
        for observer in self._observers:
            observer.update(operation, action)
class Observer:
    def __init__(self, operation, action):
        self.operation = operation
        self.action = action
    def update(self, operation, action):
        if operation is self.operation:
            self.action(operation, action)