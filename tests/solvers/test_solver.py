import numpy
from sudoku import Puzzle
import pytest
from sudoku.solvers import IterativeSolver, ParallelSolver, RecursiveSolver
from sudoku.puzzle_serializer import PuzzleSerializer


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


def test_samples_2():
    puzzle = load_sample('./samples/puzzle2.txt')
    for solver in [RecursiveSolver, ParallelSolver]:
        target = solver()
        assert target.solve(puzzle)


def test_samples_3():
    puzzle = load_sample('./samples/puzzle3.txt')
    for solver in [IterativeSolver]:
        target = solver()
        assert target.solve(puzzle)


def test_samples_6():
    puzzle = load_sample('./samples/puzzle6.txt')
    for solver in [IterativeSolver]:
        target = solver()
        assert target.solve(puzzle)


def load_sample(path: str):
    with open(path, 'r') as file:
        definition = file.read()
        return PuzzleSerializer.deserialize(definition)
