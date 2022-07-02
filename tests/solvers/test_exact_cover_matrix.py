from numpy import array
from sudoku.puzzle import Puzzle
from sudoku.solvers.exact_cover_matrix import ExactCoverMatrix


def test_simple_solution():
    puzzle = Puzzle(grid=array([[1, 2, 3, 4],
                                [2, 3, 4, 1],
                                [3, 4, 1, 2],
                                [4, 1, 2, None]]))
    target = ExactCoverMatrix.build_from(puzzle)
