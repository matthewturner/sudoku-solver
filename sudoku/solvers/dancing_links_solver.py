from concurrent.futures.thread import _threads_queues
from sudoku.solvers.link_matrix import LinkMatrix
from .. import Puzzle
from .exact_cover_matrix import ExactCoverMatrix


class DancingLinksSolver:
    def __init__(self):
        self.change_listener = None

    def solve(self, puzzle: Puzzle):
        matrix = ExactCoverMatrix.build_from(puzzle)
        matrix.clear_clues()

        link_matrix = LinkMatrix.build_from(matrix.matrix)
        solved, solutions = link_matrix.search()

        if not solved:
            return False

        for row in solutions:
            value = (row % puzzle.size) + 1
            solution_index = row // puzzle.size
            c = solution_index % puzzle.size
            r = solution_index // puzzle.size
            if not puzzle.has_value(c, r):
                puzzle.set(c, r, value)

        return _threads_queues
