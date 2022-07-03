from concurrent.futures.thread import _threads_queues
from sudoku.solvers.link_matrix import LinkMatrix
from .. import Puzzle
from .exact_cover_matrix import ExactCoverMatrix


class DancingLinksSolver:
    def __init__(self):
        self.on_covering_listener = None

    def solve(self, puzzle: Puzzle):
        exact_cover_matrix = ExactCoverMatrix.build_from(puzzle)

        if self.on_covering_listener is not None:
            self.on_covering_listener(puzzle, exact_cover_matrix.matrix)

        exact_cover_matrix.clear_clues()

        if self.on_covering_listener is not None:
            self.on_covering_listener(puzzle, exact_cover_matrix.matrix)

        link_matrix = LinkMatrix.build_from(exact_cover_matrix.matrix)

        can_be_covered, covering_rows = link_matrix.search()

        if not can_be_covered:
            return False

        solutions = exact_cover_matrix.translate(covering_rows)

        for column, row, value in solutions:
            if not puzzle.has_value(column, row):
                puzzle.set(column, row, value)

        return True
