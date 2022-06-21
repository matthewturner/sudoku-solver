from column import Column
import pytest


def test_is_valid():
    values = [[1, 2, None, 4],
              [None, 1, 2, 4]]
    target = Column(0, values)
    actual = target.is_valid(2)
    assert actual


def test_is_valid():
    values = [[1, None, None, 4],
              [2, 1, 3, 4]]
    target = Column(0, values)
    actual = not target.is_valid(2)
    assert actual
