from .. import Puzzle
from .binary_matrix import BinaryMatrix


class DancingLinksSolver:
    def __init__(self):
        self.change_listener = None

    def solve(self, puzzle: Puzzle):
        matrix = BinaryMatrix.build_from(puzzle)
