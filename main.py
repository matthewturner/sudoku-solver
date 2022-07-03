import sys

from numpy import array
from sudoku import *
from sudoku.solvers.dancing_links_solver import DancingLinksSolver
from sudoku.solvers.exact_cover_matrix import ExactCoverMatrix
from sudoku.solvers.link_matrix import LinkMatrix


def print_state(puzzle: Puzzle):
    definition = PuzzleSerializer.serialize(puzzle)
    print(definition)


def print_matrix(puzzle: Puzzle, matrix: array):
    print('Candate:  ', end='')
    for i in range(0, matrix.shape[0]):
        print(f'{(i % puzzle.size) + 1}|', end='')
    print()

    count = 0
    width = 100
    for row in matrix:
        print(f'{count}:  '.rjust(10), end='')
        for index, column in enumerate(row):
            if index >= width:
                break
            if (column):
                print('1|', end='')
            else:
                print('.|', end='')
        count += 1
        print()
    print()


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

    solver = DancingLinksSolver()

    solver.on_covering_listener = print_matrix

    if solver.solve(puzzle):
        print()
        print('Solution found:')
        print()

        definition = PuzzleSerializer.serialize(puzzle)
        print(definition)

        print()
    else:
        print('No solution found')


if __name__ == '__main__':
    main()
