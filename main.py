from sudoku import *

file = open('./samples/puzzle2.txt', 'r')
definition = file.read()
file.close()

puzzle = PuzzleSerializer.deserialize(definition)

print()

definition = PuzzleSerializer.serialize(puzzle)
print(definition)

print()

solver = Solver()
solver.solve(puzzle)

print()

definition = PuzzleSerializer.serialize(puzzle)
print(definition)

print()
