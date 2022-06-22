from sudoku import Square


def test_is_valid():
    grid = [[1, 2, None, 4],
            [None, 1, 2, 4],
            [1, 2, 4, None],
            [1, None, 2, 4]]
    target = Square(grid)
    actual = target.is_valid(1, 0, 3)
    assert actual


def test_is_not_valid():
    grid = [[1, 3, None, 4],
            [None, 1, 2, 4],
            [1, 2, 4, None],
            [1, None, 2, 4]]
    target = Square(grid)
    actual = not target.is_valid(0, 1, 3)
    assert actual


def test_is_valid_second():
    grid = [[1, 3, None, 4],
            [None, 1, 2, 4],
            [1, 2, 4, None],
            [1, None, 2, 4]]
    target = Square(grid)
    actual = target.is_valid(1, 3, 3)
    assert actual


def test_is_not_valid_second():
    grid = [[1, 3, None, 4],
            [None, 1, 2, 4],
            [1, 3, 4, None],
            [1, None, 2, 4]]
    target = Square(grid)
    actual = not target.is_valid(1, 3, 3)
    assert actual


def test_is_valid_third():
    grid = [[None, None, None, 4],
            [None, None, 2, 4],
            [None, None, 4, None],
            [None, None, 2, 4]]
    target = Square(grid)
    actual = target.is_valid(2, 0, 3)
    assert actual
