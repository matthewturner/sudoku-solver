import numpy
from .. import Puzzle


class BinaryMatrix:
    def __init__(self, column_count: int, row_count: int):
        self.matrix = numpy.empty(
            shape=(row_count, column_count), dtype='bool')

    def build_from(puzzle: Puzzle):
        # width includes cell contraint
        column_count = puzzle.size * len(puzzle.constraints)
        row_count = puzzle.size ^ 3
        matrix = BinaryMatrix(column_count, row_count)
        # for row in range(0, puzzle.size ^ 2):
        #     for column in range(0, puzzle.size):
        #         matrix.matrix[row, column] =

        return matrix
