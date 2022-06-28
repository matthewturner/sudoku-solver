import numpy
from .. import Puzzle


class BinaryMatrix:
    def __init__(self, matrix: numpy.array):
        self.matrix = matrix

    def build_from(puzzle: Puzzle):
        column_count = puzzle.size * len(puzzle.constraints)
        row_count = puzzle.size ** 3

        matrix = numpy.full(
            shape=(row_count, column_count), fill_value=False, dtype='bool')

        bm = BinaryMatrix(matrix)

        bm.__apply_cell_constraint(puzzle)
        bm.__apply_row_constraint(puzzle)
        bm.__apply_column_constraint(puzzle)
        bm.__apply_box_constraint(puzzle)

        return bm

    def __apply_cell_constraint(self, puzzle: Puzzle):
        column = -1
        for row in range(0, len(self.matrix)):
            if row % puzzle.size == 0:
                column += 1
            self.matrix[row, column] = True

    def __apply_row_constraint(self, puzzle: Puzzle):
        padding = -puzzle.size
        for row in range(0, len(self.matrix)):
            if row % puzzle.size ** 2 == 0:
                padding += puzzle.size
            column = row % puzzle.size + padding
            self.matrix[row, column] = True

    def __apply_column_constraint(self, puzzle: Puzzle):
        padding = -puzzle.size
        for row in range(0, len(self.matrix)):
            if row % puzzle.size == 0:
                padding += puzzle.size
            if row % puzzle.size ** 2 == 0:
                padding = 0
            column = row % puzzle.size + padding
            self.matrix[row, column] = True

    def __apply_box_constraint(self, puzzle: Puzzle):
        pass
