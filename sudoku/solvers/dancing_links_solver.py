from .. import Puzzle
from .exact_cover_matrix import ExactCoverMatrix


class DancingLinksSolver:
    def __init__(self):
        self.change_listener = None

    def solve(self, puzzle: Puzzle):
        matrix = ExactCoverMatrix.build_from(puzzle)
        matrix.clear_clues()
