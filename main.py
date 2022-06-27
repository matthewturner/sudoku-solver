import sys
from sudoku import *
from sudoku.solvers.binary_matrix import BinaryMatrix


def print_state(puzzle: Puzzle):
    definition = PuzzleSerializer.serialize(puzzle)
    print(definition)


def main():
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

    solver = IterativeSolver()

    solver.change_listener = print_state

    if solver.solve(puzzle):
        print()
        print('Solution found:')
        print()

        definition = PuzzleSerializer.serialize(puzzle)
        print(definition)

        print()
    else:
        print('No solution found')


def binary_matrix():
    matrix = BinaryMatrix.build_from(Puzzle(4))
    count = 0
    for row in matrix.matrix:
        print(f'{count}:  '.rjust(6), end='')
        for column in row:
            if (column):
                print(' 1', end='')
            else:
                print(' 0', end='')
        count += 1
        print()
        # if count == 30:
        #     break
    print()
    print()


if __name__ == '__main__':
    # main()
    binary_matrix()
