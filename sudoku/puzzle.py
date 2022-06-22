import array
from math import sqrt
from . import Row, Column, Square


class Puzzle:
    def __init__(self, size: int = None, grid: array = None):
        if size is None and grid is None:
            raise ValueError('Size or grid must be supplied')

        if size is None:
            size = len(grid)
        if not sqrt(size).is_integer():
            raise ValueError(f'{size} is not a square')
        self.size = size

        if grid is None:
            self.grid = [[None for _ in range(size)] for _ in range(size)]
        else:
            if True in (len(row) != size for row in grid):
                raise ValueError('Grid is malformed')
            self.grid = grid

        self.rules = [Row(self.grid),
                      Column(self.grid),
                      Square(self.grid)]

    def is_valid(self, column: int, row: int, value: int):
        self.__validate_dimensions(column, row)

        for rule in self.rules:
            if not rule.is_valid(column, row, value):
                return False

        return True

    def has_value(self, column: int, row: int):
        return not self.value(column, row) is None

    def value(self, column: int, row: int):
        self.__validate_dimensions(column, row)

        return self.grid[row][column]

    def try_set(self, column: int, row: int, value: int):
        if self.is_valid(column, row, value):
            self.__safe_set(column, row, value)
            return True

        return False

    def clear(self, column: int, row: int):
        self.__validate_dimensions(column, row)
        self.__safe_set(column, row, None)

    def set(self, column: int, row: int, value: int):
        self.__validate_dimensions(column, row)

        if value < 1:
            raise ValueError(f'{value} must be between 1 and {self.size}')

        if value > self.size:
            raise ValueError(f'{value} exceeds max value of {self.size}')

        if not self.is_valid(column, row, value):
            raise ValueError(
                f'{value} is not valid at location ({column},{row})')

        self.__safe_set(column, row, value)

    def __safe_set(self, column: int, row: int, value: int):
        self.grid[row][column] = value

    def __validate_dimensions(self, column, row):
        if column >= self.size:
            raise IndexError(f'{column} exceeds max value of {self.size - 1}')
        if row >= self.size:
            raise IndexError(f'{row} exceeds max value of {self.size - 1}')
