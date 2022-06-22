from sudoku import Puzzle, PuzzleSerializer


def test_serialize():
    expected = ' ' + '''
 _ _ _ _
 _ _ _ _
 _ _ _ _
 _ _ _ _
    '''.strip() + '\n'
    actual = PuzzleSerializer.serialize(Puzzle(4))
    assert expected == actual


def test_deserialize():
    expected = ' ' + '''
 _ _ _ _
 _ _ _ _
 _ _ 3 _
 4 _ _ _
    '''.strip() + '\n'
    puzzle = PuzzleSerializer.deserialize(expected)
    actual = PuzzleSerializer.serialize(puzzle)
    assert expected == actual
