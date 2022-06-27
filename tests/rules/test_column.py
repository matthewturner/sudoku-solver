from sudoku.constraints import Column
from sudoku.puzzle import Puzzle


def test_is_valid():
    grid = [[1, 2, None, 4],
            [None, 1, 2, 4]]
    target = Column(grid, [])
    actual = target.is_valid(0, 1, 2)
    assert actual


def test_is_valid():
    grid = [[1, None, None, 4],
            [2, 1, 3, 4],
            [None, None, None, None],
            [None, None, None, None]]
    target = Column(grid, [])
    actual = not target.is_valid(0, 1, 2)
    assert actual
