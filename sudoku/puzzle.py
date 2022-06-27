import array
from math import sqrt

import numpy
from . import Cell, Row, Column, Box


class Puzzle:
    def __init__(self, size: int = None, grid: numpy.array = None, candidates: array = None):
        if size is None and grid is None:
            raise ValueError('Size or grid must be supplied')

        if size is None:
            size = len(grid)
        if not sqrt(size).is_integer():
            raise ValueError(f'{size} is not a square')
        self.size = size

        if grid is None:
            self.grid = numpy.array(
                [[None for _ in range(size)] for _ in range(size)])
        else:
            if True in (len(row) != size for row in grid):
                raise ValueError('Grid is malformed')
            self.grid = grid

        if candidates is None:
            self.candidates = range(1, self.size + 1)
        else:
            self.candidates = candidates

        self.constraints = [Cell(self.grid, self.candidates),
                            Row(self.grid, self.candidates),
                            Column(self.grid, self.candidates),
                            Box(self.grid, self.candidates)]

    def is_valid(self, column: int, row: int, value: int):
        self.__validate_value(value)

        for constraint in self.constraints:
            if not constraint.is_valid(column, row, value):
                return False

        return True

    def has_value(self, column: int, row: int):
        return not self.value(column, row) is None

    def value(self, column: int, row: int):
        return self.grid[row, column]

    def try_set(self, column: int, row: int, value: int):
        self.__validate_value(value)

        if self.is_valid(column, row, value):
            self.grid[row, column] = value
            return True

        return False

    def set(self, column: int, row: int, value: int):
        if not self.try_set(column, row, value):
            raise ValueError(
                f'{value} is not valid at location ({column},{row})')

    def clear(self, column: int, row: int):
        self.grid[row, column] = None

    def update_from(self, other):
        for row in range(0, self.size):
            for column in range(0, self.size):
                self.grid[column, row] = other.grid[column, row]

    def __validate_value(self, value):
        if not value in self.candidates:
            raise ValueError(f'{value} must be one of {self.candidates}')
