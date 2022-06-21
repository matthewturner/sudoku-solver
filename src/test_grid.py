from puzzle import Puzzle
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
