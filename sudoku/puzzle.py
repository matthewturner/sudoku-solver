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
            for row in grid:
                if len(row) != size:
                    raise ValueError('Grid is malformed')
            self.grid = grid

        self.rows = [Row(index, self.grid)
                     for index in range(self.size)]

        self.columns = [Column(index, self.grid)
                        for index in range(self.size)]

        self.squares = [Square(index, self.grid)
                        for index in range(self.size)]

    def is_valid(self, column: int, row: int, value: int):
        self.__validate_dimensions(column, row)

        if not self.columns[column].is_valid(value):
            return False

        if not self.rows[row].is_valid(value):
            return False

        if not self.square_at(column, row).is_valid(value):
            return False

        return True

    def square_at(self, column: int, row: int):
        for sq in self.squares:
            if row in sq.rows and column in sq.columns:
                return sq
        return None

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

        if value > self.size:
            raise ValueError(f'{value} exceeds max value of {self.size}')

        if value < 1:
            raise ValueError(f'{value} must be between 1 and {self.size}')

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
