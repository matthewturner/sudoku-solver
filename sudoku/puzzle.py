from math import sqrt
from . import Row, Column, Square


class Puzzle:
    def __init__(self, scale: int):
        if sqrt(scale).is_integer() is False:
            raise ValueError(f'{scale} is not a square')

        self.scale = scale
        self.grid = [[None for _ in range(scale)] for _ in range(scale)]

        self.rows = [Row(index, self.grid)
                     for index in range(scale)]

        self.columns = [Column(index, self.grid)
                        for index in range(scale)]

        self.squares = [Square(index, self.grid)
                        for index in range(scale)]

    def is_valid(self, column: int, row: int, value: int):
        self.validate_dimensions(column, row)

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
        self.validate_dimensions(column, row)

        return self.grid[row][column]

    def set_value(self, column: int, row: int, value: int):
        self.validate_dimensions(column, row)

        if value > self.scale:
            raise ValueError(f'{value} exceeds max value of {self.scale}')

        if not self.is_valid(column, row, value):
            raise ValueError(
                f'{value} is not valid at location ({column},{row})')

        self.grid[row][column] = value

    def validate_dimensions(self, column, row):
        if column >= self.scale:
            raise IndexError(f'{column} exceeds max value of {self.scale - 1}')
        if row >= self.scale:
            raise IndexError(f'{row} exceeds max value of {self.scale - 1}')
