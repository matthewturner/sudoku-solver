import numpy
from .. import Puzzle


class BinaryMatrix:
    def __init__(self, matrix: numpy.array):
        self.matrix = matrix
        self.row = 0

    def build_from(puzzle: Puzzle):
        column_count = (puzzle.size ** 2) * len(puzzle.constraints)
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
            self.matrix[self.row, column] = True
            # self.row += 1

    def __apply_row_constraint(self, puzzle: Puzzle):
        padding = -puzzle.size
        for row in range(0, len(self.matrix)):
            if row % puzzle.size ** 2 == 0:
                padding += puzzle.size
            column = row % puzzle.size + padding
            self.matrix[self.row, column] = True
            # self.row += 1

    def __apply_column_constraint(self, puzzle: Puzzle):
        padding = -puzzle.size
        for row in range(0, len(self.matrix)):
            if row % puzzle.size == 0:
                padding += puzzle.size
            if row % puzzle.size ** 2 == 0:
                padding = 0
            column = row % puzzle.size + padding
            self.matrix[self.row, column] = True
            # self.row += 1

    def __apply_box_constraint(self, puzzle: Puzzle):
        box_size = int(numpy.sqrt(puzzle.size))
        for br in range(0, puzzle.size, box_size):
            for bc in range(0, puzzle.size, box_size):
                for n in range(0, puzzle.size):
                    for r_delta in range(0, box_size):
                        for c_delta in range(0, box_size):
                            column = self.__calculate_column(
                                puzzle, br + r_delta, bc + c_delta, n)
                            print((column, self.row))
                            self.matrix[self.row, column] = True
                    self.row += 1

    def __calculate_column(self, puzzle: Puzzle, row: int, column: int, iteration: int):
        return row * puzzle.size * puzzle.size + column * puzzle.size + iteration
