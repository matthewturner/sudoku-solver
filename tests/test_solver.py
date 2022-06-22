from sudoku import Puzzle, Solver
import pytest


def test_simple_solution():
    puzzle = Puzzle(4, [[1, 2, 3, 4],
                        [2, 3, 4, 1],
                        [3, 4, 1, 2],
                        [4, 1, 2, None]])
    target = Solver()
    target.solve(puzzle)
    assert puzzle.value(3, 3) == 3
