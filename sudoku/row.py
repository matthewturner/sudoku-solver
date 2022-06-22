from array import array


class Row:
    def __init__(self, index: int, grid: array):
        self.index = index
        self.grid = grid

    def is_valid(self, value: int):
        return not value in self.grid[self.index]
