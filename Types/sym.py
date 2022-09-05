import math


class Sym:

    def __init__(self, col_position, col_name):
        self.items_seen = 0
        self.col_pos = col_position or 0
        self.col_name = col_name or ""
        self.symbol_dictionary = {}

    def add(self, symbol):
        if symbol != "?":
            self.items_seen = self.items_seen + 1
            self.symbol_dictionary[symbol] = self.symbol_dictionary.get(symbol, 0) + 1

    def mid(self, col_position):
        most = -1
        mode = None
        for symbol, occurrence in self.symbol_dictionary.items():
            if occurrence > most:
                mode = symbol
                most = occurrence

        return mode

    def div(self):
        e = 0

        def f(p):
            return p * math.log(p, 2)

        for symbol, occurrence in self.symbol_dictionary.items():
            if occurrence > 0:
                e = e + f(symbol/self.items_seen)

        return e
