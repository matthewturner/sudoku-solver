from sudoku import Row


def test_is_valid():
    target = Row(0, [[1, 2, None, 4]])
    actual = target.is_valid(3)
    assert actual


def test_is_valid():
    target = Row(0, [[1, 2, None, 4]])
    actual = not target.is_valid(2)
    assert actual
