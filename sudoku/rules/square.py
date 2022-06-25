import numpy
from math import sqrt


class Square:
    def __init__(self, grid: numpy.array):
        self.grid = grid
        self.size = int(sqrt(len(grid)))

    def is_valid(self, column: int, row: int, value: int):
        row_first_index = int(row / self.size) * self.size
        row_last_index = row_first_index + self.size

        column_first_index = int(column / self.size) * self.size
        column_last_index = column_first_index + self.size

        for rows in self.grid[row_first_index:row_last_index]:
            if value in rows[column_first_index:column_last_index]:
                return False

        return True
