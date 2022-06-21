from math import sqrt


class Grid:
    def __init__(self, scale: int):
        if sqrt(scale).is_integer() is False:
            raise ValueError(f'{scale} is not a square')

        self.scale = scale
        self.values = [[None for _ in range(scale)] for _ in range(scale)]
        self.rows = []
        self.columns = []
        self.squares = []

    def value(self, column: int, row: int):
        self.validate_dimensions(column, row)

        return self.values[row][column]

    def set_value(self, column: int, row: int, value: int):
        self.validate_dimensions(column, row)

        if value > self.scale:
            raise ValueError(f'{value} exceeds max value of {self.scale}')

        self.values[row][column] = value

    def validate_dimensions(self, column, row):
        if column >= self.scale:
            raise IndexError(f'{column} exceeds max value of {self.scale - 1}')
        if row >= self.scale:
            raise IndexError(f'{row} exceeds max value of {self.scale - 1}')
