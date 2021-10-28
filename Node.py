class Node:
    def __init__(self, symbol, value):
        self._symbol = symbol
        self._value = value
        self._next = None

    @property
    def symbol(self):
        return self._symbol

    @property
    def value(self):
        return self._value

    @property
    def next(self):
        return self._next

    @symbol.setter
    def symbol(self, symbol):
        self._symbol = symbol

    @value.setter
    def value(self, value):
        self._value = value

    @next.setter
    def next(self, next):
        self._next = next

    def __str__(self):
        return "Symbol:  " + str(self._symbol) + " | Value:  " + str(self._value) + " | Next: ( " + str(self._next) + " )"
