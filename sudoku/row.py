from array import array


class Row:
    def __init__(self, index: int, values: array):
        self.index = index
        self.values = values

    def is_valid(self, value: int):
        return not value in self.values[self.index]
