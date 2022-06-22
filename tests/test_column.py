from sudoku import Column


def test_is_valid():
    grid = [[1, 2, None, 4],
              [None, 1, 2, 4]]
    target = Column(0, grid)
    actual = target.is_valid(2)
    assert actual


def test_is_valid():
    grid = [[1, None, None, 4],
              [2, 1, 3, 4]]
    target = Column(0, grid)
    actual = not target.is_valid(2)
    assert actual
