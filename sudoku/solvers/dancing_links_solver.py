from concurrent.futures.thread import _threads_queues
from sudoku.solvers.link_matrix import LinkMatrix
from .. import Puzzle
from .exact_cover_matrix import ExactCoverMatrix


class DancingLinksSolver:
    def __init__(self):
        self.on_matrix_built_listener = None
        self.on_clues_filtered_listener = None
        self.on_covered_listener = None
        self.on_solution_found = None
        self.on_partial_solution_found = None

    def solve(self, puzzle: Puzzle):
        exact_cover_matrix = ExactCoverMatrix.build_from(puzzle)

        if self.on_matrix_built_listener is not None:
            self.on_matrix_built_listener(puzzle, exact_cover_matrix)

        exact_cover_matrix.clear_clues()

        if self.on_clues_filtered_listener is not None:
            self.on_clues_filtered_listener(puzzle, exact_cover_matrix)

        link_matrix = LinkMatrix.build_from(exact_cover_matrix.matrix)

        can_be_covered, covering_rows = link_matrix.search()

        if not can_be_covered:
            return False

        if self.on_covered_listener is not None:
            self.on_covered_listener(puzzle, exact_cover_matrix, covering_rows)

        solutions = exact_cover_matrix.translate(covering_rows)

        solution_rows = []
        for exact_row_index, column, row, value in solutions:
            if not puzzle.has_value(column, row):
                solution_rows.append(exact_row_index)
                puzzle.set(column, row, value)

        if self.on_solution_found is not None:
            self.on_covered_listener(puzzle, exact_cover_matrix, solution_rows)

        if len(covering_rows) < puzzle.size ** 2:
            if self.on_partial_solution_found is not None:
                self.on_partial_solution_found(puzzle)
            return False

        return True
