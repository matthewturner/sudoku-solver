from array import array


class Row:
    def __init__(self, grid: array):
        self.grid = grid

    def is_valid(self, _: int, row: int, value: int):
        return not value in self.grid[row]
