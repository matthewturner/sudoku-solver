from square import Square
import pytest


def test_is_valid():
    values = [[1, 2, None, 4],
              [None, 1, 2, 4],
              [1, 2, 4, None],
              [1, None, 2, 4]]
    target = Square(0, values)
    actual = target.is_valid(3)
    assert actual


def test_is_not_valid():
    values = [[1, 3, None, 4],
              [None, 1, 2, 4],
              [1, 2, 4, None],
              [1, None, 2, 4]]
    target = Square(0, values)
    actual = not target.is_valid(3)
    assert actual


def test_is_valid_second():
    values = [[1, 3, None, 4],
              [None, 1, 2, 4],
              [1, 2, 4, None],
              [1, None, 2, 4]]
    target = Square(1, values)
    actual = target.is_valid(3)
    assert actual


def test_is_not_valid_second():
    values = [[1, 3, None, 4],
              [None, 1, 2, 4],
              [1, 3, 4, None],
              [1, None, 2, 4]]
    target = Square(1, values)
    actual = not target.is_valid(3)
    assert actual


def test_is_valid_third():
    values = [[None, None, None, 4],
              [None, None, 2, 4],
              [None, None, 4, None],
              [None, None, 2, 4]]
    target = Square(2, values)
    actual = target.is_valid(3)
    assert actual
