from sudoku import *

file = open('./samples/puzzle1.txt', 'r')
definition = file.read()
file.close()

puzzle = PuzzleSerializer.deserialize(definition)

puzzle.set_value(8, 8, 8)

print()

definition = PuzzleSerializer.serialize(puzzle)
print(definition)

print()
