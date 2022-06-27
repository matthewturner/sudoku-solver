
from math import sqrt

from numpy import array
from .base import Base


class Box(Base):
    def __init__(self, grid: array, candidates: list):
        self.size = int(sqrt(len(grid)))
        Base.__init__(self, grid, candidates)

    def is_valid(self, column: int, row: int, value: int):
        row_first_index = int(row / self.size) * self.size
        row_last_index = row_first_index + self.size

        column_first_index = int(column / self.size) * self.size
        column_last_index = column_first_index + self.size

        for rows in self.grid[row_first_index:row_last_index]:
            if value in rows[column_first_index:column_last_index]:
                return False

        return True
