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
                    value = self.puzzle.value(c, r)
                    for n in range(0, self.puzzle.size):
                        if value == self.puzzle.candidates[n]:
                            pass
                        else:
                            row_index = self.__calculate_row_index(r, c, n)
                            self.matrix[row_index] = False

    def translate(self, rows: list[int]) -> tuple:
        '''Translates a list of covering rows to puzzle solutions'''
        solutions = []
        for row in rows:
            value = self.puzzle.candidates[(row % self.puzzle.size)]
            solution_index = row // self.puzzle.size
            c = solution_index % self.puzzle.size
            r = solution_index // self.puzzle.size
            solutions.append((c, r, value))
        return solutions

    @staticmethod
    def build_from(puzzle: Puzzle):
        column_count = (puzzle.size ** 2) * len(puzzle.constraints)
        row_count = puzzle.size ** 3

        matrix = numpy.full(
            shape=(row_count, column_count), fill_value=False, dtype='bool')

        ecm = ExactCoverMatrix(matrix, puzzle)
        column_index = 0
        column_index = ecm.__apply_cell_constraint(column_index)
        column_index = ecm.__apply_row_constraint(column_index)
        column_index = ecm.__apply_column_constraint(column_index)
        column_index = ecm.__apply_box_constraint(column_index)
        return ecm

    def __apply_cell_constraint(self, column_index: int):
        size = self.puzzle.size
        for r in range(0, size):
            for c in range(0, size):
                for n in range(0, size):
                    row_index = self.__calculate_row_index(r, c, n)
                    self.matrix[row_index, column_index] = True
                column_index += 1
        return column_index

    def __apply_row_constraint(self, column_index: int):
        size = self.puzzle.size
        for r in range(0, size):
            for n in range(0, size):
                for c in range(0, size):
                    row_index = self.__calculate_row_index(r, c, n)
                    self.matrix[row_index, column_index] = True
                column_index += 1
        return column_index

    def __apply_column_constraint(self, column_index: int):
        size = self.puzzle.size
        for c in range(0, size):
            for n in range(0, size):
                for r in range(0, size):
                    row_index = self.__calculate_row_index(r, c, n)
                    self.matrix[row_index, column_index] = True
                column_index += 1
        return column_index

    def __apply_box_constraint(self, column_index: int):
        size = self.puzzle.size
        box_size = int(numpy.sqrt(size))
        for br in range(0, size, box_size):
            for bc in range(0, size, box_size):
                for n in range(0, size):
                    for r_delta in range(0, box_size):
                        for c_delta in range(0, box_size):
                            row_index = self.__calculate_row_index(
                                br + r_delta, bc + c_delta, n)
                            self.matrix[row_index, column_index] = True
                    column_index += 1
        return column_index

    def __calculate_row_index(self, row: int, column: int, iteration: int):
        size = self.puzzle.size
        return (row * size * size) + (column * size) + iteration
