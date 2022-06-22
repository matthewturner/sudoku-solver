from array import array


class Column:
    def __init__(self, index: int, grid: array):
        self.index = index
        self.grid = grid

    def is_valid(self, value: int):
        for row in self.grid:
            if row[self.index] == value:
                return False
        return True
