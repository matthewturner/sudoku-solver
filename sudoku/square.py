from array import array
from math import sqrt


class Square:
    def __init__(self, index: int, grid: array):
        self.index = index
        self.grid = grid
        self.size = int(sqrt(len(grid)))

        row_first_index = (self.index % self.size) * self.size
        row_last_index = row_first_index + self.size
        self.rows = range(row_first_index, row_last_index)

        column_first_index = int(self.index / self.size) * self.size
        column_last_index = column_first_index + self.size
        self.columns = range(column_first_index, column_last_index)

    def is_valid(self, value: int):
        for rows in self.grid[self.rows.start:self.rows.stop]:
            if value in rows[self.columns.start:self.columns.stop]:
                return False

        return True
