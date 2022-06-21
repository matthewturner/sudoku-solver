from array import array


class Column:
    def __init__(self, index: int, values: array):
        self.index = index
        self.values = values

    def is_valid(self, value: int):
        for row in self.values:
            if row[self.index] == value:
                return False
        return True
