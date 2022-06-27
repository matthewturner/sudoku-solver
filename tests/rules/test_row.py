from sudoku import Row
from sudoku.puzzle import Puzzle


def test_is_valid():
    target = Row([[1, 2, None, 4],
                  [None, None, None, None],
                  [None, None, None, None],
                  [None, None, None, None]])
    actual = target.is_valid(2, 0, 3)
    assert actual


def test_is_valid():
    target = Row([[1, 2, None, 4],
                  [None, None, None, None],
                  [None, None, None, None],
                  [None, None, None, None]], [])
    actual = not target.is_valid(2, 0, 2)
    assert actual
