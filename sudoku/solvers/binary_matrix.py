import numpy
from .. import Puzzle


class BinaryMatrix:
    def __init__(self, matrix: numpy.array):
        self.matrix = matrix

    def build_from(puzzle: Puzzle):
        column_count = (puzzle.size ** 2) * len(puzzle.constraints)
        row_count = puzzle.size ** 3

        matrix = numpy.full(
            shape=(row_count, column_count), fill_value=False, dtype='bool')

        row = 0
        row = BinaryMatrix.__apply_cell_constraint(matrix, puzzle.size, row)
        row = BinaryMatrix.__apply_row_constraint(matrix, puzzle.size, row)
        row = BinaryMatrix.__apply_column_constraint(matrix, puzzle.size, row)
        row = BinaryMatrix.__apply_box_constraint(matrix, puzzle.size, row)

        return BinaryMatrix(matrix)

    def __apply_cell_constraint(matrix: numpy.array, size: int, row: int):
        for r in range(0, size):
            for c in range(0, size):
                for n in range(0, size):
                    column = BinaryMatrix.__calculate_column(
                        size, r, c, n)
                    # print(f"{r}, {column}, {n} -> {(column, self.row)}")
                    matrix[column, row] = True
                row += 1
        return row

    def __apply_row_constraint(matrix: numpy.array, size: int, row: int):
        for r in range(0, size):
            for n in range(0, size):
                for c in range(0, size):
                    column = BinaryMatrix.__calculate_column(
                        size, r, c, n)
                    # print(f"{r}, {column}, {n} -> {(column, self.row)}")
                    matrix[column, row] = True
                row += 1
        return row

    def __apply_column_constraint(matrix: numpy.array, size: int, row: int):
        for c in range(0, size):
            for n in range(0, size):
                for r in range(0, size):
                    column = BinaryMatrix.__calculate_column(
                        size, r, c, n)
                    # print(f"{r}, {column}, {n} -> {(column, self.row)}")
                    matrix[column, row] = True
                row += 1
        return row

    def __apply_box_constraint(matrix: numpy.array, size: int, row: int):
        box_size = int(numpy.sqrt(size))
        for br in range(0, size, box_size):
            for bc in range(0, size, box_size):
                for n in range(0, size):
                    for r_delta in range(0, box_size):
                        for c_delta in range(0, box_size):
                            column = BinaryMatrix.__calculate_column(
                                size, br + r_delta, bc + c_delta, n)
                            # print(f"{r}, {column}, {n} -> {(column, self.row)}")
                            matrix[column, row] = True
                    row += 1
        return row

    def __calculate_column(size: int, row: int, column: int, iteration: int):
        return (row * size * size) + (column * size) + iteration
