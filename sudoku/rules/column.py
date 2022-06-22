from array import array


class Column:
    def __init__(self, grid: array):
        self.grid = grid

    def is_valid(self, column: int, _: int, value: int):
        for row in self.grid:
            if row[column] == value:
                return False
        return True
