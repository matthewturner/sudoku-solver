from sudoku import Puzzle
import pytest


def test_square_number():
    assert Puzzle(4)


def test_non_square_number():
    with pytest.raises(ValueError):
        Puzzle(5)


def test_value_at_index():
    target = Puzzle(4)
    target.set_value(2, 2, 4)
    assert target.value(2, 2) == 4


def test_is_valid_based_on_row():
    target = Puzzle(4)
    target.set_value(0, 0, 1)
    assert target.is_valid(1, 2, 1)


def test_is_not_valid_based_on_row():
    target = Puzzle(4)
    target.set_value(0, 0, 1)
    assert not target.is_valid(1, 0, 1)


def test_is_valid_based_on_column():
    target = Puzzle(4)
    target.set_value(0, 0, 1)
    assert target.is_valid(2, 1, 1)


def test_is_not_valid_based_on_column():
    target = Puzzle(4)
    target.set_value(0, 0, 1)
    assert not target.is_valid(0, 1, 1)


def test_is_not_valid_based_on_square():
    target = Puzzle(9)
    target.set_value(0, 0, 1)
    assert not target.is_valid(1, 1, 1)
