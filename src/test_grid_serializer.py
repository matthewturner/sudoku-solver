from grid import Grid
from grid_serializer import GridSerializer
import pytest


def test_serialize():
    expected = ' ' + '''
 _ _ _ _
 _ _ _ _
 _ _ _ _
 _ _ _ _
    '''.strip() + '\n'
    actual = GridSerializer.serialize(Grid(4))
    assert expected == actual


def test_deserialize():
    expected = ' ' + '''
 _ _ _ _
 _ _ _ _
 _ _ 3 _
 4 _ _ _
    '''.strip() + '\n'
    grid = GridSerializer.deserialize(expected)
    actual = GridSerializer.serialize(grid)
    assert expected == actual
