from array import array
from math import sqrt


class Square:
    def __init__(self, index: int, values: array):
        self.index = index
        self.values = values
        self.scale = int(sqrt(len(values)))

        row_first_index = (self.index % self.scale) * self.scale
        row_last_index = row_first_index + self.scale
        self.rows = range(row_first_index, row_last_index)

        column_first_index = int(self.index / self.scale) * self.scale
        column_last_index = column_first_index + self.scale
        self.columns = range(column_first_index, column_last_index)

    def is_valid(self, value: int):
        for rows in self.values[self.rows.start:self.rows.stop]:
            if value in rows[self.columns.start:self.columns.stop]:
                return False

        return True
