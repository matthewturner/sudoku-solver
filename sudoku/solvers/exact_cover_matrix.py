import numpy
from .. import Puzzle


class ExactCoverMatrix:
    def __init__(self, matrix: numpy.array, puzzle: Puzzle):
        self.matrix = matrix
        self.puzzle = puzzle

    def clear_clues(self):
        '''Zeroes out the grid where clues already exist in the puzzle'''
        for r in range(0, self.puzzle.size):
            for c in range(0, self.puzzle.size):
                if self.puzzle.has_value(c, r):
                    for n in range(0, self.puzzle.size):
                        column = self.__calculate_column(r, c, n)
                        self.matrix[column] = False

    def build_from(puzzle: Puzzle):
        column_count = (puzzle.size ** 2) * len(puzzle.constraints)
        row_count = puzzle.size ** 3

        matrix = numpy.full(
            shape=(row_count, column_count), fill_value=False, dtype='bool')

        bm = ExactCoverMatrix(matrix, puzzle)
        row = 0
        row = bm.__apply_cell_constraint(row)
        row = bm.__apply_row_constraint(row)
        row = bm.__apply_column_constraint(row)
        row = bm.__apply_box_constraint(row)
        return bm

    def __apply_cell_constraint(self, row: int):
        size = self.puzzle.size
        for r in range(0, size):
            for c in range(0, size):
                for n in range(0, size):
                    column = self.__calculate_column(r, c, n)
                    # print(f"{r}, {column}, {n} -> {(column, self.row)}")
                    self.matrix[column, row] = True
                row += 1
        return row

    def __apply_row_constraint(self, row: int):
        size = self.puzzle.size
        for r in range(0, size):
            for n in range(0, size):
                for c in range(0, size):
                    column = self.__calculate_column(r, c, n)
                    # print(f"{r}, {column}, {n} -> {(column, self.row)}")
                    self.matrix[column, row] = True
                row += 1
        return row

    def __apply_column_constraint(self, row: int):
        size = self.puzzle.size
        for c in range(0, size):
            for n in range(0, size):
                for r in range(0, size):
                    column = self.__calculate_column(r, c, n)
                    # print(f"{r}, {column}, {n} -> {(column, self.row)}")
                    self.matrix[column, row] = True
                row += 1
        return row

    def __apply_box_constraint(self, row: int):
        size = self.puzzle.size
        box_size = int(numpy.sqrt(size))
        for br in range(0, size, box_size):
            for bc in range(0, size, box_size):
                for n in range(0, size):
                    for r_delta in range(0, box_size):
                        for c_delta in range(0, box_size):
                            column = self.__calculate_column(
                                br + r_delta, bc + c_delta, n)
                            # print(f"{r}, {column}, {n} -> {(column, self.row)}")
                            self.matrix[column, row] = True
                    row += 1
        return row

    def __calculate_column(self, row: int, column: int, iteration: int):
        size = self.puzzle.size
        return (row * size * size) + (column * size) + iteration
