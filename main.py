from sudoku import *

file = open('./samples/puzzle3.txt', 'r')
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


def print_state(puzzle: Puzzle):
    definition = PuzzleSerializer.serialize(puzzle)
    print(definition)


solver.row_change_listener = print_state

if solver.solve(puzzle):
    print('Solution found:')
    print()

    definition = PuzzleSerializer.serialize(puzzle)
    print(definition)

    print()
else:
    print('No solution found')
