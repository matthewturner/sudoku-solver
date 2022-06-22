from sudoku import Puzzle, Solver
import pytest


def test_simple_solution():
    puzzle = Puzzle(grid=[[1, 2, 3, 4],
                          [2, 3, 4, 1],
                          [3, 4, 1, 2],
                          [4, 1, 2, None]])
    target = Solver()
    target.solve(puzzle)
    assert puzzle.value(3, 3) == 3


def test_moderate_solution():
    puzzle = Puzzle(grid=[[1, 2, 3, 4],
                          [3, 4, None, 2],
                          [2, None, 4, 1],
                          [4, 1, 2, 3]])
    target = Solver()
    target.solve(puzzle)
    assert puzzle.value(2, 1) == 1
    assert puzzle.value(1, 2) == 3
