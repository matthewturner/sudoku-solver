import numpy
from sudoku import Puzzle
import pytest
from sudoku.iterative_solver import IterativeSolver
from sudoku.parallel_solver import ParallelSolver
from sudoku.recursive_solver import RecursiveSolver


def test_simple_solution():
    puzzle = Puzzle(grid=numpy.array([[1, 2, 3, 4],
                          [2, 3, 4, 1],
                          [3, 4, 1, 2],
                          [4, 1, 2, None]]))
    for solver in [RecursiveSolver, IterativeSolver, ParallelSolver]:
        target = solver()
        target.solve(puzzle)
        assert puzzle.value(3, 3) == 3


def test_moderate_solution():
    puzzle = Puzzle(grid=numpy.array([[1, 2, 3, 4],
                          [3, 4, None, 2],
                          [2, None, 4, 1],
                          [4, 1, 2, 3]]))
    for solver in [RecursiveSolver, IterativeSolver, ParallelSolver]:
        target = solver()
        target.solve(puzzle)
        assert puzzle.value(2, 1) == 1
        assert puzzle.value(1, 2) == 3
