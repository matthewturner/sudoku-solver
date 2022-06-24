import sys
from sudoku import *

path = sys.argv[1] if len(sys.argv) > 1 else './samples/puzzle2.txt'

file = open(path, 'r')
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

max_column = 0


def print_state(location: tuple, puzzle: Puzzle):
    column, _ = location
    global max_column
    if column >= max_column:
        max_column = column
        definition = PuzzleSerializer.serialize(puzzle)
        print(definition)


solver.column_change_listener = print_state

if solver.solve(puzzle):
    print('Solution found:')
    print()

    definition = PuzzleSerializer.serialize(puzzle)
    print(definition)

    print()
else:
    print('No solution found')
