from sudoku import *

file = open('./samples/puzzle2.txt', 'r')
definition = file.read()
file.close()

puzzle = PuzzleSerializer.deserialize(definition)

print()
print('Puzzle:')
print()

definition = PuzzleSerializer.serialize(puzzle)
print(definition)

print()

solver = Solver()
if solver.solve(puzzle):
    print('Solution found:')
    print()

    definition = PuzzleSerializer.serialize(puzzle)
    print(definition)

    print()
else:
    print('No solution found')
